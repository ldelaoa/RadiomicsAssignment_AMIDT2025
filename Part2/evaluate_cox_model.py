def evaluate_cox_model(fitted_model, test_data, feature_names):
    test_prepared = test_data[['Survival.time', 'deadstatus.event'] + feature_names].dropna()
    partial_hazards = fitted_model.predict_partial_hazard(test_prepared)
    test_data['partial_hazards'] = partial_hazards
    c_index = concordance_index(test_prepared['Survival.time'], -partial_hazards, test_prepared['deadstatus.event'])
    results = {'concordance_index': c_index, 'feature_importance': dict(zip(feature_names, abs(fitted_model.params_)))}
    return results,test_data
