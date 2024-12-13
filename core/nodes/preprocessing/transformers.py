from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler, RobustScaler



SCALERS = {
    "standard": {'scaler': StandardScaler, 'params': {'with_mean': True, 'with_std': True}},
    "minmax": {'scaler': MinMaxScaler, 'params': {'feature_range': (0, 1)}},
    "maxabs": {'scaler': MaxAbsScaler, 'params': {}},
    "robust": {'scaler': RobustScaler, 'params': {'quantile_range': (25.0, 75.0)}},
}

