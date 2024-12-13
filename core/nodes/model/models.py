from sklearn.linear_model import LogisticRegression, LinearRegression, Lasso, Ridge, RidgeClassifier, ElasticNet, SGDClassifier, SGDRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor, BaggingRegressor
from sklearn.svm import LinearSVC, SVC, SVR, LinearSVR
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingClassifier, AdaBoostClassifier, BaggingClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier


MODELS = {
    'linear_models':
    {
    'regression':
        {
        'linear_regression':{'model': LinearRegression,'params': {}},
        'ridge':{'model': Ridge,'params': {'alpha': 1.0,}},
        'lasso':{'model': Lasso,'params': {'alpha': 1.0,}},
        'elastic_net':{'model': ElasticNet,'params': {'alpha': 1.0, 'l1_ratio': 0.5,}},
        'sgd_regression':{'model': SGDRegressor,'params': {'penalty': 'l2',}},
        },
    'classification':
        {
        'logistic_regression':{'model': LogisticRegression,'params': {'penalty': 'l2','C': 1.0,}},
        'ridge_classifier':{'model': RidgeClassifier,'params': {'alpha': 1.0,}},
        'sgd_classifier':{'model': SGDClassifier,'params': {'penalty': 'l2',}},
        }
    },
    'svm':
    {
    'regression':
        {
        'svr':{'model': SVR,'params': {'C': 1.0, 'kernel': 'rbf',}},
        'linear_svr':{'model': LinearSVR,'params': {'C': 1.0,}},
        },
    'classification':
        {
        'linear_svm':{'model': LinearSVC,'params': {'C': 1.0,}},
        'rbf_svc':{'model': SVC,'params': {'C': 1.0, 'kernel': 'rbf',}},
        'poly_svc':{'model': SVC,'params': {'C': 1.0, 'kernel': 'poly',}},
        'sigmoid_svc':{'model': SVC,'params': {'C': 1.0, 'kernel': 'sigmoid',}},
        }
    },
    'tree':
    {
    'classification':
        {
        'decision_tree':{'model': DecisionTreeClassifier,'params': {'max_depth': None,}},
        'random_forest':{'model': RandomForestClassifier,'params': {'n_estimators': 100,'max_depth': None,}},
        'gradient_boosting':{'model': GradientBoostingClassifier,'params': {}},
        'adaboost':{'model': AdaBoostClassifier,'params': {}},
        'bagging':{'model': BaggingClassifier,'params': {}},
        },
    'regression':
        {
        'decision_tree':{'model': DecisionTreeRegressor,'params': {'max_depth': None,}},
        'random_forest':{'model': RandomForestRegressor,'params': {'n_estimators': 100,'max_depth': None,}},
        'gradient_boosting':{'model': GradientBoostingRegressor,'params': {}},
        'adaboost':{'model': AdaBoostRegressor,'params': {}},
        'bagging':{'model': BaggingRegressor,'params': {}},
        },
    },
    'naive_bayes':
    {
    'regression':
    {
    },
    'classification':
        {
            'gaussian_nb':{'model': GaussianNB,'params': {}},
            'multinomial_nb':{'model': MultinomialNB,'params': {}},
            'bernoulli_nb':{'model': BernoulliNB,'params': {}},
        }
    },
    'knn':
    {
    'regression':
        {'knnr':{'model': KNeighborsRegressor,'params': {'n_neighbors': 5,}},
        },
    'classification':
        {'knnc':{'model': KNeighborsClassifier,'params': {'n_neighbors': 5,}},
    }
    },
}