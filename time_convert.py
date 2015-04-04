class time:
    def __init__(self,timestamp_list: [str]):
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
        test = ''
        if len(self.minutes) == 1:
            test = '0' + self.minutes
        else:
            test = self.minutes
             
        if len(self.seconds) == 1:
            test = test + '0' + self.seconds
        else:
            test = test + 'self.seconds'
        return test
 
if __name__ == '__main__':
    a = time(['00:01','02:33','23:33'])
    print(a.to_seconds())


