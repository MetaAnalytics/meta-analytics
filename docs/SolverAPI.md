# SolverAPI

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_vars** | **int** | Number of variables in QUBO matrix | [optional] 
**non_zero** | **int** | Number of non-zero entries in QUBO matrix | [optional] 
**timeout** | **int** | Number of seconds the algorithm can run | [optional] 
**min_max** | **int** | Specificy minimize ( 0 ) or maximize ( 1 ). Default is set to 3600. | [optional] 
**parameters** | **str** | &lt;br /&gt;-pr Path-Relinking enabled by default                &lt;br /&gt;-T  Target -- defined local minimum or maximum              &lt;br /&gt;-g  Greediness -- percentage between 0 and 1 ( default is 0 )              &lt;br /&gt;-K  num_threads -- number of simultaneous searches to perform ( default to 1 )              &lt;br /&gt;-pf Perturb Factor -- defaults to number of vars / 10. If at a minimum / max and attempt to escape               &lt;br /&gt;-rl Restart Limit -- Number of times hit same value before restarting search. Similar to MST multi-start tabu search              &lt;br /&gt;-sm Spincycle Multiplier -- Amount to multiple spincycle, if turned on. Another way to escape from local optima.              &lt;br /&gt;-sp Spincycle Percentage -- between 0 and 1 ( default 0 ) -- affects speed and accuracy              &lt;br /&gt;-it Inner Timelimit -- may speed up problems if more time is spent ( default 5 )              &lt;br /&gt;-ar Accuracy Range -- accuracy vs speed -- default 5 -- between 1 and 20                &lt;br /&gt;-am Accuracy Minimum -- define bottom end of accuracy. add range. default is 5, 1 is hill climbing | [optional] 
**solved_value** | **float** |  | [optional] 
**solved_result** | **list[int]** |  | [optional] 
**inputs** | [**list[Points]**](Points.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

