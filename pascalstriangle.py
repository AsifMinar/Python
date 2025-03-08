'''
def generate(numRows):
    # If they ask for 0 rows, give back an empty list
    if numRows == 0:
        return []
    
    # Start the triangle with the first row: [1]
    triangle = [[1]]
    
    # Add more rows, one at a time, up to numRows
    for i in range(1, numRows):
        # Get the row we made last time
        prev_row = triangle[-1]
        
        # Every row starts with a 1
        new_row = [1]
        
        # Fill in the middle by adding pairs from the previous row
        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])
        
        # Every row ends with a 1
        new_row.append(1)
        
        # Add this new row to our triangle
        triangle.append(new_row)
    
    # Give back the finished triangle
    return triangle
'''

def generate(numRows):
  
    if numRows == 0:
        return []
    
    triangle = [[1]]
    
    for i in range(1, numRows):

        prev_row = triangle[-1]
        
        new_row = [1]
        
        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])
        
        new_row.append(1)
        
        triangle.append(new_row)
    
    return triangle