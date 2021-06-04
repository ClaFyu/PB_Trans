# example

### h5 -> pb
> run```python .\h5_to_pb.py .\h5_model\(your-model's-name).h5 .\(your-model's-name).pb```, then you will get pb file in result


### ckpt -> pb
> 运行```python .\ckpt_node_names.py .\ckpt_model\(your-name)\(your-model's-name).ckpt-(number)```，得到所有节点名称，一般使用最后一个</br>
> 运行```python .\ckpt_to_pb.py .\ckpt_model\(your-model's-name)\(your-model's-name).ckpt-(number) .\result\(your-model's-name).pb (your-model's-nodename)```，在result目录下得到pb文件
