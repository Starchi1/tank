import sqlite3


class Help_db:
    def delete_db(self):
        con = sqlite3.connect("/Users/Владимир/PycharmProjects/pythonProject5/tank.sqlite")
        cur = con.cursor()
        cur.execute("DELETE FROM tanki")
        con.commit()
        con.close()

    def vivod(self):
        con = sqlite3.connect("/Users/Владимир/PycharmProjects/pythonProject5/tank.sqlite")
        cur = con.cursor()
        asd = cur.execute('SELECT * FROM tanki').fetchall()
        con.close()
        return asd

    def add_db(self, time, bullet, winner_tank):
        con = sqlite3.connect("/Users/Владимир/PycharmProjects/pythonProject5/tank.sqlite")
        cur = con.cursor()
        all = cur.execute('SELECT * FROM tanki').fetchall()
        cur.execute('INSERT INTO tanki(id, time, shoot, winner) VALUES(?, ?, ?, ?)',
                    (len(all) + 1, str(time), str(bullet), winner_tank))
        con.commit()
        con.close()
