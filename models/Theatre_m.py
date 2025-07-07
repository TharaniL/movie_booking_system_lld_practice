from screen_m import Screen

class Theatre:
    def __init__(self,th_id,th_name,th_loc):
        self.th_id=th_id
        self.th_name=th_name
        self.th_loc=th_loc
        self.screens=[]
        self.shows=[]



    def create_screens(self,scr_id,scr_no,rows,cols):
        screen = Screen(scr_id, scr_no, rows, cols)


        for sc in self.screens:
            if scr_id == sc.scr_id:
                return "Duplicate Screen ID or number"

        self.screens.append(screen)
        return "Screen Added Successfully"

    def create_shows(self,sh_id,sh_time,sh_date,scr_num):
        for screen in self.screens:
            if screen.scr_no==scr_num:
                screen.add_shows(sh_id,sh_time,sh_date)




