# -*- coding: utf-8 -*-
"""Set regressor function."""

__author__ = ["TonyBagnall", "MatthewMiddlehurst"]

import numpy as np
from sklearn.pipeline import make_pipeline

from tsml_eval.estimators.regression.column_ensemble import ColumnEnsembleRegressor
from tsml_eval.utils.functions import str_in_nested_list

convolution_based_regressors = [
    ["RocketRegressor", "rocket"],
    ["minirocket", "minirocketregressor"],
    ["multirocket", "multirocketregressor"],
    ["HydraRegressor", "hydra"],
    ["Arsenal", "arsenalregressor"],
]
deep_learning_regressors = [
    ["CNNRegressor", "cnn"],
    ["TapNetRegressor", "tapnet"],
    ["ResNetRegressor", "resnet"],
    ["InceptionTimeRegressor", "inception", "inceptiontime"],
    ["IndividualInceptionTimeRegressor", "singleinception", "individualinception"],
    ["FCNRegressor", "fcnn", "fcn"],
]
dictionary_based_regressors = [
    ["TemporalDictionaryEnsemble", "tde"],
]
distance_based_regressors = [
    ["KNeighborsTimeSeriesRegressor", "1nn-ed"],
    "5nn-ed",
    "1nn-dtw",
    "5nn-dtw",
]
feature_based_regressors = [
    ["FreshPRINCERegressor", "fresh-prince", "freshprince"],
    "freshprince-500",
]
hybrid_regressors = [
    ["HIVECOTEV2", "hc2"],
]
interval_based_regressors = [
    ["TimeSeriesForestRegressor", "tsf"],
    "tsf-i",
    "tsf-500",
    "DrCIF",
    "drcif-500",
]
other_regressors = [
    ["DummyRegressor", "dummy", "dummyregressor-tsml"],
    "dummyregressor-aeon",
    "dummyregressor-sklearn",
    ["MeanPredictorRegressor", "dummymeanpred"],
    ["MedianPredictorRegressor", "dummymedianpred"],
    ["FPCRegressor", "fpcr"],
    "fpcr-b-spline",
]
shapelet_based_regressors = [
    "str-2hour",
    ["ShapeletTransformRegressor", "str", "stc"],
    "str-2hour-ridge",
]
vector_regressors = [
    ["RotationForest", "rotf"],
    ["LinearRegression", "lr"],
    ["RidgeCV", "ridge"],
    ["SVR", "svm", "supportvectorregressor"],
    ["grid-svr", "grid-svm", "grid-supportvectorregressor"],
    ["RandomForestRegressor", "rf", "randomforest"],
    ["randomforest-500", "rf-500"],
    ["XGBRegressor", "xgboost"],
    ["xgb-100", "xgboost-100"],
    ["xgb-500", "xgboost-500"],
]


def set_regressor(
    regressor_name,
    random_state=None,
    n_jobs=1,
    build_train_file=False,
    fit_contract=0,
    checkpoint=None,
    **kwargs,
):
    """Return a regressor matching a given input name.

    Basic way of creating a regressor to build using the default or alternative
    settings. This set up is to help with batch jobs for multiple problems and to
    facilitate easy reproducibility through run_regression_experiment.

    Generally, inputting a regressor class name will return said regressor with
    default settings.

    Parameters
    ----------
    regressor_name : str
        String indicating which regressor to be returned.
    random_state : int, RandomState instance or None, default=None
        Random seed or RandomState object to be used in the regressor if available.
    build_train_file : bool, default=False
        Whether a train data results file is being produced. If True, regressor specific
        parameters for generating train results will be toggled if available.
    n_jobs: int, default=1
        The number of jobs to run in parallel for both regressor ``fit`` and
        ``predict`` if available. `-1` means using all processors.
    fit_contract: int, default=0
        Contract time in minutes for regressor ``fit`` if available.

    Return
    ------
    regressor: A BaseRegressor.
        The regressor matching the input regressor name.
    """
    r = regressor_name.lower()

    if str_in_nested_list(convolution_based_regressors, r):
        return _set_regressor_convolution_based(
            r, random_state, n_jobs, build_train_file, fit_contract, checkpoint, kwargs
        )
    elif str_in_nested_list(deep_learning_regressors, r):
        return _set_regressor_deep_learning(
            r, random_state, n_jobs, build_train_file, fit_contract, checkpoint, kwargs
        )
    elif str_in_nested_list(dictionary_based_regressors, r):
        return _set_regressor_dictionary_based(
            r, random_state, n_jobs, build_train_file, fit_contract, checkpoint, kwargs
        )
    elif str_in_nested_list(distance_based_regressors, r):
        return _set_regressor_distance_based(
            r, random_state, n_jobs, build_train_file, fit_contract, checkpoint, kwargs
        )
    elif str_in_nested_list(feature_based_regressors, r):
        return _set_regressor_feature_based(
            r, random_state, n_jobs, build_train_file, fit_contract, checkpoint, kwargs
        )
    elif str_in_nested_list(hybrid_regressors, r):
        return _set_regressor_hybrid(
            r, random_state, n_jobs, build_train_file, fit_contract, checkpoint, kwargs
        )
    elif str_in_nested_list(interval_based_regressors, r):
        return _set_regressor_interval_based(
            r, random_state, n_jobs, build_train_file, fit_contract, checkpoint, kwargs
        )
    elif str_in_nested_list(other_regressors, r):
        return _set_regressor_other(
            r, random_state, n_jobs, build_train_file, fit_contract, checkpoint, kwargs
        )
    elif str_in_nested_list(shapelet_based_regressors, r):
        return _set_regressor_shapelet_based(
            r, random_state, n_jobs, build_train_file, fit_contract, checkpoint, kwargs
        )
    elif str_in_nested_list(vector_regressors, r):
        return _set_regressor_vector(
            r, random_state, n_jobs, build_train_file, fit_contract, checkpoint, kwargs
        )
    else:
        raise ValueError(f"UNKNOWN REGRESSOR {r} in set_regressor")


def _set_regressor_convolution_based(
    r, random_state, n_jobs, build_train_file, fit_contract, checkpoint, kwargs
):
    if r == "rocketregressor" or r == "rocket":
        from aeon.regression.convolution_based import RocketRegressor

        return RocketRegressor(random_state=random_state, n_jobs=n_jobs, **kwargs)
    elif r == "minirocket" or r == "minirocketregressor":
        from aeon.regression.convolution_based import RocketRegressor

        return RocketRegressor(
            rocket_transform="minirocket",
            random_state=random_state,
            n_jobs=n_jobs,
            **kwargs,
        )
    elif r == "multirocket" or r == "multirocketregressor":
        from aeon.regression.convolution_based import RocketRegressor

        return RocketRegressor(
            rocket_transform="multirocket",
            random_state=random_state,
            n_jobs=n_jobs,
            **kwargs,
        )
    elif r == "hydraregressor" or r == "hydra":
        from tsml_eval.estimators.regression.convolution_based import HydraRegressor

        return HydraRegressor(random_state=random_state, n_jobs=n_jobs, **kwargs)
    elif r == "arsenal" or r == "arsenalregressor":
        from tsml_eval.estimators.regression.convolution_based import Arsenal

        return Arsenal(
            random_state=random_state,
            n_jobs=n_jobs,
            save_transformed_data=build_train_file,
            time_limit_in_minutes=fit_contract,
            **kwargs,
        )


def _set_regressor_deep_learning(
    r, random_state, n_jobs, build_train_file, fit_contract, checkpoint, kwargs
):
    if r == "cnnregressor" or r == "cnn":
        from sktime.regression.deep_learning.cnn import CNNRegressor

        return CNNRegressor(random_state=random_state, **kwargs)
    elif r == "tapnetregressor" or r == "tapnet":
        from sktime.regression.deep_learning.tapnet import TapNetRegressor

        return TapNetRegressor(random_state=random_state, **kwargs)
    elif r == "resnetregressor" or r == "resnet":
        from tsml_eval.estimators.regression.deep_learning import ResNetRegressor

        return ResNetRegressor(random_state=random_state, **kwargs)
    elif r == "inceptiontimeregressor" or r == "inception" or r == "inceptiontime":
        from tsml_eval.estimators.regression.deep_learning import InceptionTimeRegressor

        return InceptionTimeRegressor(random_state=random_state, **kwargs)
    elif (
        r == "individualinceptiontimeregressor"
        or r == "singleinception"
        or r == "individualinception"
    ):
        from tsml_eval.estimators.regression.deep_learning import (
            IndividualInceptionTimeRegressor,
        )

        return IndividualInceptionTimeRegressor(random_state=random_state, **kwargs)
    elif r == "fcnregressor" or r == "fcnn" or r == "fcn":
        from tsml_eval.estimators.regression.deep_learning import FCNRegressor

        return FCNRegressor(random_state=random_state, **kwargs)


def _set_regressor_dictionary_based(
    r, random_state, n_jobs, build_train_file, fit_contract, checkpoint, kwargs
):
    if r == "temporaldictionaryensemble" or r == "tde":
        from tsml_eval.estimators.regression.dictionary_based import (
            TemporalDictionaryEnsemble,
        )

        return TemporalDictionaryEnsemble(
            random_state=random_state,
            n_jobs=n_jobs,
            save_train_predictions=build_train_file,
            time_limit_in_minutes=fit_contract,
            **kwargs,
        )


def _set_regressor_distance_based(
    r, random_state, n_jobs, build_train_file, fit_contract, checkpoint, kwargs
):
    if r == "kneighborstimeseriesregressor" or r == "1nn-ed":
        from tsml_eval.estimators.regression.distance_based import (
            KNeighborsTimeSeriesRegressor,
        )

        return KNeighborsTimeSeriesRegressor(**kwargs)
    elif r == "5nn-ed":
        from tsml_eval.estimators.regression.distance_based import (
            KNeighborsTimeSeriesRegressor,
        )

        return KNeighborsTimeSeriesRegressor(n_neighbors=5, **kwargs)
    elif r == "1nn-dtw":
        from tsml_eval.estimators.regression.distance_based import (
            KNeighborsTimeSeriesRegressor,
        )

        return KNeighborsTimeSeriesRegressor(
            distance="dtw", distance_params={"window": 0.1}, **kwargs
        )
    elif r == "5nn-dtw":
        from tsml_eval.estimators.regression.distance_based import (
            KNeighborsTimeSeriesRegressor,
        )

        return KNeighborsTimeSeriesRegressor(
            n_neighbors=5, distance="dtw", distance_params={"window": 0.1}, **kwargs
        )
    elif r == "1nn-msm":
        from tsml_eval.estimators.regression.distance_based import (
            KNeighborsTimeSeriesRegressor,
        )

        return KNeighborsTimeSeriesRegressor(
            n_neighbors=1,
            distance="msm",
            distance_params={"window": None, "independent": True, "c": 1},
        )
    elif r == "5nn-msm":
        from tsml_eval.estimators.regression.distance_based import (
            KNeighborsTimeSeriesRegressor,
        )

        return KNeighborsTimeSeriesRegressor(
            n_neighbors=5,
            distance="msm",
            distance_params={"window": None, "independent": True, "c": 1},
        )


def _set_regressor_feature_based(
    r, random_state, n_jobs, build_train_file, fit_contract, checkpoint, kwargs
):
    if r == "freshprinceregressor" or r == "fresh-prince" or r == "freshprince":
        from tsml_eval.estimators.regression.featured_based import FreshPRINCERegressor

        return FreshPRINCERegressor(
            random_state=random_state,
            n_jobs=n_jobs,
            save_transformed_data=build_train_file,
            **kwargs,
        )
    elif r == "freshprince-500":
        from tsml_eval.estimators.regression.featured_based import FreshPRINCERegressor

        return FreshPRINCERegressor(
            n_estimators=500,
            random_state=random_state,
            n_jobs=n_jobs,
            save_transformed_data=build_train_file,
            **kwargs,
        )


def _set_regressor_hybrid(
    r, random_state, n_jobs, build_train_file, fit_contract, checkpoint, kwargs
):
    if r == "hivecotev2" or r == "hc2":
        from tsml_eval.estimators.regression.hybrid import HIVECOTEV2

        return HIVECOTEV2(
            random_state=random_state,
            n_jobs=n_jobs,
            time_limit_in_minutes=fit_contract,
            **kwargs,
        )


def _set_regressor_interval_based(
    r, random_state, n_jobs, build_train_file, fit_contract, checkpoint, kwargs
):
    if r == "timeseriesforestregressor" or r == "tsf":
        from aeon.regression.interval_based import TimeSeriesForestRegressor

        return TimeSeriesForestRegressor(
            random_state=random_state, n_jobs=n_jobs, **kwargs
        )
    elif r == "tsf-i":
        from aeon.regression.interval_based import TimeSeriesForestRegressor

        estimators = [
            (
                "tsf",
                TimeSeriesForestRegressor(random_state=random_state, n_jobs=n_jobs),
                None,
            )
        ]

        return ColumnEnsembleRegressor(estimators, **kwargs)
    elif r == "tsf-500":
        from aeon.regression.interval_based import TimeSeriesForestRegressor

        return TimeSeriesForestRegressor(
            n_estimators=500, random_state=random_state, n_jobs=n_jobs, **kwargs
        )
    elif r == "drcif":
        from tsml_eval.estimators.regression.interval_based import DrCIF

        return DrCIF(
            random_state=random_state,
            n_jobs=n_jobs,
            save_transformed_data=build_train_file,
            time_limit_in_minutes=fit_contract,
            **kwargs,
        )
    elif r == "drcif-500":
        from tsml_eval.estimators.regression.interval_based import DrCIF

        return DrCIF(
            n_estimators=500,
            random_state=random_state,
            n_jobs=n_jobs,
            save_transformed_data=build_train_file,
            time_limit_in_minutes=fit_contract,
            **kwargs,
        )


def _set_regressor_other(
    r, random_state, n_jobs, build_train_file, fit_contract, checkpoint, kwargs
):
    if r == "dummy" or r == "dummyregressor" or r == "dummyregressor-tsml":
        from tsml.dummy import DummyRegressor

        return DummyRegressor(**kwargs)
    elif r == "dummyregressor-aeon":
        from aeon.regression.dummy import DummyRegressor

        return DummyRegressor(**kwargs)
    elif r == "dummyregressor-sklearn":
        from sklearn.dummy import DummyRegressor

        return DummyRegressor(**kwargs)
    elif r == "meanpredictorregressor" or r == "dummymeanpred":
        # the dummy regressor is to predict the mean value of the output.
        from tsml_eval.estimators.regression.dummy import MeanPredictorRegressor

        return MeanPredictorRegressor(**kwargs)
    elif r == "medianpredictorregressor" or r == "dummymedianpred":
        # the dummy regressor is to predict the mean value of the output.
        from tsml_eval.estimators.regression.dummy import MedianPredictorRegressor

        return MedianPredictorRegressor(**kwargs)
    elif r == "fpcregressor" or r == "fpcr":
        from tsml_eval.estimators.regression.sofr import FPCRegressor

        return FPCRegressor(n_jobs=n_jobs, **kwargs)
    elif r == "fpcr-b-spline":
        from tsml_eval.estimators.regression.sofr import FPCRegressor

        return FPCRegressor(
            n_jobs=n_jobs, smooth="B-spline", order=4, n_basis=10, **kwargs
        )


def _set_regressor_shapelet_based(
    r, random_state, n_jobs, build_train_file, fit_contract, checkpoint, kwargs
):
    if r == "str-2hour":
        from tsml_eval.estimators.regression.shapelet_based import (
            ShapeletTransformRegressor,
        )

        return ShapeletTransformRegressor(
            transform_limit_in_minutes=120,
            random_state=random_state,
            n_jobs=n_jobs,
            save_transformed_data=build_train_file,
            time_limit_in_minutes=fit_contract,
            **kwargs,
        )
    elif r == "shapelettransformregressor" or r == "str" or r == "stc":
        from tsml_eval.estimators.regression.shapelet_based import (
            ShapeletTransformRegressor,
        )

        return ShapeletTransformRegressor(
            random_state=random_state,
            n_jobs=n_jobs,
            save_transformed_data=build_train_file,
            time_limit_in_minutes=fit_contract,
            **kwargs,
        )
    elif r == "str-2hour-ridge":
        from sklearn.linear_model import RidgeCV
        from sklearn.preprocessing import StandardScaler

        from tsml_eval.estimators.regression.shapelet_based import (
            ShapeletTransformRegressor,
        )

        return ShapeletTransformRegressor(
            estimator=make_pipeline(
                StandardScaler(with_mean=False),
                RidgeCV(alphas=np.logspace(-3, 3, 10)),
            ),
            transform_limit_in_minutes=120,
            random_state=random_state,
            n_jobs=n_jobs,
            save_transformed_data=build_train_file,
            time_limit_in_minutes=fit_contract,
            **kwargs,
        )


def _set_regressor_vector(
    r, random_state, n_jobs, build_train_file, fit_contract, checkpoint, kwargs
):
    if r == "rotationforest" or r == "rotf":
        from tsml_eval.estimators.regression.sklearn import RotationForest

        return RotationForest(
            random_state=random_state,
            n_jobs=n_jobs,
            save_transformed_data=build_train_file,
            time_limit_in_minutes=fit_contract,
            **kwargs,
        )
    elif r == "linearregression" or r == "lr":
        from sklearn.linear_model import LinearRegression

        return LinearRegression(fit_intercept=True, n_jobs=n_jobs, **kwargs)
    elif r == "ridgecv" or r == "ridge":
        from sklearn.linear_model import RidgeCV

        return RidgeCV(fit_intercept=True, alphas=np.logspace(-3, 3, 10), **kwargs)
    elif r == "svr" or r == "svm" or r == "supportvectorregressor":
        from sklearn.svm import SVR

        return SVR(kernel="rbf", C=1, **kwargs)
    elif r == "grid-svr" or r == "grid-svm" or r == "grid-supportvectorregressor":
        from sklearn.model_selection import GridSearchCV
        from sklearn.svm import SVR

        param_grid = [
            {
                "kernel": ["rbf", "sigmoid"],
                "C": [0.1, 1, 10, 100],
                "gamma": [0.001, 0.01, 0.1, 1],
            }
        ]

        return GridSearchCV(
            estimator=SVR(),
            param_grid=param_grid,
            scoring="neg_mean_squared_error",
            n_jobs=n_jobs,
            cv=3,
            **kwargs,
        )
    elif r == "randomforestregressor" or r == "rf" or r == "randomforest":
        from sklearn.ensemble import RandomForestRegressor

        return RandomForestRegressor(random_state=random_state, n_jobs=n_jobs, **kwargs)
    elif r == "rf-500" or r == "randomforest-500":
        from sklearn.ensemble import RandomForestRegressor

        return RandomForestRegressor(
            n_estimators=500, random_state=random_state, n_jobs=n_jobs, **kwargs
        )
    elif r == "xgbregressor" or r == "xgboost":
        from xgboost import XGBRegressor

        return XGBRegressor(random_state=random_state, n_jobs=n_jobs, **kwargs)
    elif r == "xgb-100" or r == "xgboost-100":
        from xgboost import XGBRegressor

        return XGBRegressor(
            n_estimators=100,
            learning_rate=0.1,
            random_state=random_state,
            n_jobs=n_jobs,
            **kwargs,
        )
    elif r == "xgb-500" or r == "xgboost-500":
        from xgboost import XGBRegressor

        return XGBRegressor(
            n_estimators=500,
            learning_rate=0.1,
            random_state=random_state,
            n_jobs=n_jobs,
            **kwargs,
        )
