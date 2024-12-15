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
        'linear_regression':{'node': LinearRegression,'params': {}},
        'ridge':{'node': Ridge,'params': {'alpha': 1.0,}},
        'lasso':{'node': Lasso,'params': {'alpha': 1.0,}},
        'elastic_net':{'node': ElasticNet,'params': {'alpha': 1.0, 'l1_ratio': 0.5,}},
        'sgd_regression':{'node': SGDRegressor,'params': {'penalty': 'l2',}},
        },
    'classification':
        {
        'logistic_regression':{'node': LogisticRegression,'params': {'penalty': 'l2','C': 1.0,}},
        'ridge_classifier':{'node': RidgeClassifier,'params': {'alpha': 1.0,}},
        'sgd_classifier':{'node': SGDClassifier,'params': {'penalty': 'l2',}},
        }
    },
    'svm':
    {
    'regression':
        {
        'svr':{'node': SVR,'params': {'C': 1.0, 'kernel': 'rbf',}},
        'linear_svr':{'node': LinearSVR,'params': {'C': 1.0,}},
        },
    'classification':
        {
        'linear_svm':{'node': LinearSVC,'params': {'C': 1.0,}},
        'rbf_svc':{'node': SVC,'params': {'C': 1.0, 'kernel': 'rbf',}},
        'poly_svc':{'node': SVC,'params': {'C': 1.0, 'kernel': 'poly',}},
        'sigmoid_svc':{'node': SVC,'params': {'C': 1.0, 'kernel': 'sigmoid',}},
        }
    },
    'tree':
    {
    'classification':
        {
        'decision_tree':{'node': DecisionTreeClassifier,'params': {'max_depth': None,}},
        'random_forest':{'node': RandomForestClassifier,'params': {'n_estimators': 100,'max_depth': None,}},
        'gradient_boosting':{'node': GradientBoostingClassifier,'params': {}},
        'adaboost':{'node': AdaBoostClassifier,'params': {}},
        'bagging':{'node': BaggingClassifier,'params': {}},
        },
    'regression':
        {
        'decision_tree':{'node': DecisionTreeRegressor,'params': {'max_depth': None,}},
        'random_forest':{'node': RandomForestRegressor,'params': {'n_estimators': 100,'max_depth': None,}},
        'gradient_boosting':{'node': GradientBoostingRegressor,'params': {}},
        'adaboost':{'node': AdaBoostRegressor,'params': {}},
        'bagging':{'node': BaggingRegressor,'params': {}},
        },
    },
    'naive_bayes':
    {
    'regression':
    {
    },
    'classification':
        {
            'gaussian_nb':{'node': GaussianNB,'params': {}},
            'multinomial_nb':{'node': MultinomialNB,'params': {}},
            'bernoulli_nb':{'node': BernoulliNB,'params': {}},
        }
    },
    'knn':
    {
    'regression':
        {'knnr':{'node': KNeighborsRegressor,'params': {'n_neighbors': 5,}},
        },
    'classification':
        {'knnc':{'node': KNeighborsClassifier,'params': {'n_neighbors': 5,}},
    }
    },
}