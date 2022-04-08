import pandas as pd 
import numpy as np 
import math

#https://stackoverflow.com/questions/22227595/convert-integer-to-binary-array-with-suitable-padding
def bin_array(num, m):
    """Convert a positive integer num into an m-bit bit vector"""
    return np.array(list(np.binary_repr(num).zfill(m)),int)

def my_binary_encoder(df, col):
	'''
	A binary encoding of the values in the column col for the DataFrame df
	Will return a dataframe with both the encoding and the origional column that has been encoded.

	Binary encoding works better than one hot encoding for a large (200 ish) number of values in trees ect as there are Log_2(N) features rather than N.
	The down side is that the distance between encodings is not root(2) but can be both smaller (min 1) and larger (max root(n-1)). 
	
	Improvment: make a class that includes a decoder?
	
	Parameters
    ----------
    df : pandas DataFrame
        The name of the animal
    col : str
        the label for the column we will be encoding 
	'''
	value_dict = pd.unique(df['a'])
	no_unique_elements = len(value_dict)
	value_dict = dict(zip(value_dict, list(range(no_unique_elements))))
	encoding_length = math.ceil(np.log2(no_unique_elements))

	binary_array = df[col].apply(lambda x:  bin_array(value_dict[x],encoding_length))
	index_list = [ col + '_' + str(val) for val in range(encoding_length)]

	df1 = pd.DataFrame(item for item in binary_array)
	df1.columns = index_list

	df = pd.concat([df, df1], axis = 1)
	
	return df

if __name__ == '__main__':
	data = {'id':[0,1,2], 'a':['Ryan', 'Jack', 'Ben']}
	df = pd.DataFrame(data)
	print('original dataframe:\n',df)
	print('\nencoded dataframe:\n',my_binary_encoder(df, 'a'))
