# example

### h5 -> pb
> run```python .\h5_to_pb.py .\h5_model\(your-model's-name).h5 .\(your-model's-name).pb```, then you will get pb file in result.


### ckpt -> pb
> run```python .\ckpt_node_names.py .\ckpt_model\(your-name)\(your-model's-name).ckpt-(number)```, then you will get all nodes' name. I usually use the last one.</br>
> run```python .\ckpt_to_pb.py .\ckpt_model\(your-model's-name)\(your-model's-name).ckpt-(number) .\result\(your-model's-name).pb (your-model's-nodename)```, then you will get pb file in result.
