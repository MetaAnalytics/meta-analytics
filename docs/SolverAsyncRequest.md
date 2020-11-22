# SolverAsyncRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** | The name of the S3 bucket to pull data from. | [optional] 
**key_name** | **str** | S3 key name. This is the specific key in the bucket. | [optional] 
**solution_bucket_name** | **str** | The name of the S3 bucket to place result data in. If empty or null, defaults to bucketName | [optional] 
**solution_key_name** | **str** | S3 key name. Key name for the result. Defaults to keyName.out if left empty. | [optional] 
**region** | **str** | AWS Region that is used for authentication.. | [optional] 
**num_vars** | **int** | Number of variables in the QUBO. | [optional] 
**min_max** | **int** | Specify 0 for minimum, or 1 for maximum. | [optional] 
**non_zero** | **int** | Number of non zero elements in the QUBO. | [optional] 
**timeout** | **int** | Max time in seconds the algorithm can run. | [optional] 
**parameters** | **str** | Additional parameters. See definition of Solver3API for details. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

