class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        paths_content = {} 

        for path in paths:
            directory, *files = path.split(' ')
            new_file = []
            for f in files:
                file_content= list(f.split('('))

                paths_content[file_content[1][:-1]] = paths_content.get(file_content[1][:-1], [])+([f'{directory}/{file_content[0]}'])


        paths_content = dict(sorted(paths_content.items(), reverse=True))


        
        ans = [path_content for path_content in paths_content.values() if len(path_content) >= 2 ]
        
        

        return ans   
        