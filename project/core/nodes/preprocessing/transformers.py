from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler, RobustScaler



SCALERS = {
    "standard_scaler": {'scaler': StandardScaler, 'params': {'with_mean': True, 'with_std': True}},
    "minmax_scaler": {'scaler': MinMaxScaler, 'params': {'feature_range': (0, 1)}},
    "maxabs_scaler": {'scaler': MaxAbsScaler, 'params': {}},
    "robust_scaler": {'scaler': RobustScaler, 'params': {'quantile_range': (25.0, 75.0)}},
}

