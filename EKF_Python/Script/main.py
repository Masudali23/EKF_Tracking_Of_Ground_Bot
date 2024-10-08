import numpy as np

# Kalman Filter Class
class KalmanFilter:
    def __init__(self):
        self.x = None  # state vector
        self.P = None  # state covariance matrix
        self.F = None  # state transition matrix
        self.Q = None  # process covariance matrix
        self.H = None  # measurement matrix
        self.R = None  # measurement covariance matrix

    def init(self, x_in, P_in, F_in, H_in, R_in, Q_in):
        self.x = x_in
        self.P = P_in
        self.F = F_in
        self.H = H_in
        self.R = R_in
        self.Q = Q_in

    def predict(self):
        self.x = np.dot(self.F, self.x)
        self.P = np.dot(np.dot(self.F, self.P), self.F.T) + self.Q

    def update(self, z):
        y = z - np.dot(self.H, self.x)
        self._update_common(y)

    def update_ekf(self, z):
        px, py, vx, vy = self.x
        rho = np.sqrt(px**2 + py**2)
        theta = np.arctan2(py, px)
        rho_dot = (px * vx + py * vy) / rho if rho > 0 else 0
        h = np.array([rho, theta, rho_dot])

        y = z - h
        y[1] = self._normalize_angle(y[1])
        self._update_common(y)

    def _update_common(self, y):
        Ht = self.H.T
        S = np.dot(self.H, np.dot(self.P, Ht)) + self.R
        K = np.dot(np.dot(self.P, Ht), np.linalg.inv(S))

        self.x = self.x + np.dot(K, y)
        I = np.eye(len(self.x))
        self.P = (I - np.dot(K, self.H)) @ self.P

    @staticmethod
    def _normalize_angle(angle):
        return (angle + np.pi) % (2 * np.pi) - np.pi


# Tools Class
class Tools:
    @staticmethod
    def calculate_jacobian(x_state):
        px, py, vx, vy = x_state
        c1 = px**2 + py**2
        if abs(c1) < 1e-4:
            return np.zeros((3, 4))

        c2 = np.sqrt(c1)
        c3 = c1 * c2

        jacobian = np.array([
            [px/c2, py/c2, 0, 0],
            [-py/c1, px/c1, 0, 0],
            [py*(vx*py - vy*px)/c3, px*(px*vy - py*vx)/c3, px/c2, py/c2]
        ])
        return jacobian

    @staticmethod
    def calculate_rmse(estimations, ground_truth):
        estimations = np.array(estimations)
        ground_truth = np.array(ground_truth)
        if len(estimations) == 0 or len(estimations) != len(ground_truth):
            raise ValueError("Invalid estimation or ground_truth data")

        residual = estimations - ground_truth
        residual = np.square(residual)
        rmse = np.sqrt(np.mean(residual, axis=0))
        return rmse


# FusionEKF Class
class FusionEKF:
    def __init__(self):
        self.is_initialized = False
        self.previous_timestamp = 0

        self.ekf = KalmanFilter()

        # Measurement covariance matrices for Lidar and Radar
        self.R_laser = np.array([[0.0225, 0], [0, 0.0225]])
        self.R_radar = np.array([[0.09, 0, 0], [0, 0.0009, 0], [0, 0, 0.09]])

        # Measurement matrix for Lidar
        self.H_laser = np.array([[1, 0, 0, 0], [0, 1, 0, 0]])

        # Process and measurement noises
        self.noise_ax = 9
        self.noise_ay = 9

    def process_measurement(self, sensor_data):
        if not self.is_initialized:
            self.initialize(sensor_data)
            self.is_initialized = True
            return

        dt = (sensor_data['timestamp'] - self.previous_timestamp) / 1000000.0
        self.previous_timestamp = sensor_data['timestamp']

        self.update_state_transition(dt)
        self.update_process_covariance(dt)

        self.ekf.predict()

        if sensor_data['sensor_type'] == 'RADAR':
            Hj = Tools.calculate_jacobian(self.ekf.x)
            self.ekf.H = Hj
            self.ekf.R = self.R_radar
            self.ekf.update_ekf(sensor_data['raw_measurements'])
        else:
            self.ekf.H = self.H_laser
            self.ekf.R = self.R_laser
            self.ekf.update(sensor_data['raw_measurements'])

    def initialize(self, sensor_data):
        x_initial = np.zeros(4)

        if sensor_data['sensor_type'] == 'RADAR':
            rho, phi, rho_dot = sensor_data['raw_measurements']
            x_initial[0] = rho * np.cos(phi)
            x_initial[1] = rho * np.sin(phi)
        else:
            x_initial[0], x_initial[1] = sensor_data['raw_measurements']

        self.ekf.x = x_initial
        self.ekf.P = np.eye(4) * 1000
        self.ekf.P[0, 0] = 1
        self.ekf.P[1, 1] = 1

        self.previous_timestamp = sensor_data['timestamp']

    def update_state_transition(self, dt):
        self.ekf.F = np.array([[1, 0, dt, 0], [0, 1, 0, dt], [0, 0, 1, 0], [0, 0, 0, 1]])

    def update_process_covariance(self, dt):
        dt_2 = dt ** 2
        dt_3 = dt ** 3
        dt_4 = dt ** 4
        qx = self.noise_ax
        qy = self.noise_ay

        self.ekf.Q = np.array([
            [dt_4 / 4 * qx, 0, dt_3 / 2 * qx, 0],
            [0, dt_4 / 4 * qy, 0, dt_3 / 2 * qy],
            [dt_3 / 2 * qx, 0, dt_2 * qx, 0],
            [0, dt_3 / 2 * qy, 0, dt_2 * qy]
        ])


# Main function to process input and generate output
def main():
    estimations = []
    ground_truth = []
    
    fusion_ekf = FusionEKF()
    tools = Tools()

    with open("EKF_Python/data/Input.txt", "r") as in_file, open("EKF_Python/Output/output.txt", "w") as out_file:
        for line in in_file:
            data = line.split()
            sensor_type = data[0]

            if sensor_type == "L":
                sensor_data = {'sensor_type': 'LASER', 
                               'raw_measurements': np.array([float(data[1]), float(data[2])]), 
                               'timestamp': int(data[3])}
            elif sensor_type == "R":
                sensor_data = {'sensor_type': 'RADAR', 
                               'raw_measurements': np.array([float(data[1]), float(data[2]), float(data[3])]), 
                               'timestamp': int(data[4])}

            gt_values = np.array([float(data[-4]), float(data[-3]), float(data[-2]), float(data[-1])])

            fusion_ekf.process_measurement(sensor_data)

            estimate = np.array([fusion_ekf.ekf.x[0], fusion_ekf.ekf.x[1], fusion_ekf.ekf.x[2], fusion_ekf.ekf.x[3]])
            estimations.append(estimate)
            ground_truth.append(gt_values)

            out_file.write(f"{estimate[0]} {estimate[1]} {estimate[2]} {estimate[3]} "
                           f"{sensor_data['raw_measurements'][0]} {sensor_data['raw_measurements'][1]} "
                           f"{gt_values[0]} {gt_values[1]} {gt_values[2]} {gt_values[3]}\n")

    rmse = tools.calculate_rmse(estimations, ground_truth)
    print("RMSE:", rmse)

if __name__ == "__main__":
    main()
