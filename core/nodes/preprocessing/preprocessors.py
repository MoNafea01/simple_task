from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler, RobustScaler





SCALERS = {
    "standard": {'scaler': StandardScaler, 'params': {}},
    "minmax": {'scaler': MinMaxScaler, 'params': {}},
    "maxabs": {'scaler': MaxAbsScaler, 'params': {}},
    "robust": {'scaler': RobustScaler, 'params': {}},
}

