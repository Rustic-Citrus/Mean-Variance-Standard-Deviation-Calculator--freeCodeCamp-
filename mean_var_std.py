import numpy as np

def calculate(list):
    if len(list) == 9:
        array = np.array(
            [
                [num for num in list[:3]],
                [num for num in list[3:6]],
                [num for num in list[6:len(list)]]
            ]
        )
    
    else: 
        raise ValueError("List must contain nine numbers.")
        
    def op_matrix(op):
        return [
            [
                op(array[:3, 0]),
                op(array[:3, 1]),
                op(array[:3, 2])            
            ],
            [
                op(array[0, :3]),
                op(array[1, :3]),
                op(array[2, :3])
            ],
            op(array)
        ]
    
    calculations = {}
    op_dict = {
        "mean": np.mean, 
        "variance": np.var, 
        "standard deviation": np.std, 
        "max": np.amax, 
        "min": np.amin, 
        "sum": np.sum
    }
    
    for op_name, op_func in op_dict.items():
        calculations[op_name] = op_matrix(op_func)

    return calculations
