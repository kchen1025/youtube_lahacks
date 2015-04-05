class time:
    def __init__(self,timestamp_list):
        self.timestamp_list = timestamp_list
           
    #converts string timestamps into int seconds  
    def to_seconds(self):
        sec_list = []
        for cur_str in self.timestamp_list:
            time_in_sec = 0
            time_in_sec += int(cur_str[4])
            time_in_sec += 10 * int(cur_str[3])
            time_in_sec += 60 * int(cur_str[1])
            time_in_sec += 60 * 10 * int(cur_str[0])
            sec_list.append(time_in_sec)         
        return sec_list

    #convert int seconds into strings 
    def to_string(self):
        return self.timestamp_list
 



