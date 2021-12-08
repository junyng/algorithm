def solution(files):
    file_attributes = dict()
    
    for file in files:
        file_attributes[file] = dict()
        file_string = list(file)
        for i, c in enumerate(file_string):
            if c.isdigit():
                file_attributes[file]['file_head'] = ''.join(file_string[:i])
                file_string = file_string[i:]
                break
        for i, c in enumerate(file_string):
            if c.isalpha():
                file_attributes[file]['file_number'] = ''.join(file_string[:i-1])
                break
            elif i == len(file_string)-1:
                file_attributes[file]['file_number'] = ''.join(file_string)
    
    sorted_file_attributes = sorted(file_attributes.items(), key=lambda file: (file[1]['file_head'].lower(), int(file[1]['file_number'])))
    file_names = list(map(lambda attributes: attributes[0], sorted_file_attributes))
    return file_names
