from seat_m import Seat

class Screen:
    def __init__(self,scr_id,scr_num,rows,cols):
        self.scr_id=scr_id
        self.scr_num=scr_num
        self.rows=rows
        self.cols=cols
        self.no_of_seats=self.get_no_of_seats()
        self.all_seats=self.create_seats()

    def get_no_of_seats(self):
        return len(self.rows)*self.cols
    def create_seats(self):
        for row in self.rows:
            for col in range(self.cols):
                seat_id=f"{row}{col}"
                if row in ["A","B"]:
                    s_type="VIP"
                    s_rate=300
                elif row in ["C","D"]:
                    s_type="Premium"
                    s_rate=200
                else:
                    s_type="Regular"
                    s_rate=100
                seat=Seat(seat_id,seat_id,s_type,"Available",s_rate)
                self.all_seats.append(seat)


        return self.all_seats