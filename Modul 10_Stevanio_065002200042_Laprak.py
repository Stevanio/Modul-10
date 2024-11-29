def index_list(data_list, index, index_berikutnya):
    x = data_list[index]
    data_list[index] = data_list[index_berikutnya]
    data_list[index_berikutnya] = x
    
def bubblesort(data_list, len_data_list):
    for index in range(len_data_list-1):
        if data_list[index] > data_list[index + 1]:
            index_list(data_list, index, index + 1)
    if len_data_list - 1 > 1:
        bubblesort(data_list, len_data_list - 1)
        
data_list = [8,-3,2,1,0,9,12,13,20,-4,29]
print(f'List yang sebelum di sorting = \n{data_list}')
bubblesort(data_list, len(data_list))
print(f'\nList yang sudah di sorting = \n{data_list}')
