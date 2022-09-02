from PIL import Image
import random
from check import get_between_day_list
from Db import Db


class Pic:
    def __init__(self):
        self.disxy = ((192, 1348), (257, 1348))
        self.detailxy = ((132, 1616), (180, 1616), (216, 1616), (542, 1616), (594, 1616), (631, 1616))
        self.timexy = ((760, 1383), (795, 1383), (814, 1383), (850, 1383), (870, 1383))

    def edit_pic(self, tb_data, day):
        body_id = random.randint(1, 9)
        body_path = f'pic/body/本体{body_id}.jpg'
        body_image = Image.open(body_path)
        body_image_copy = body_image.copy()

        dis = int(tb_data[0])
        dis1 = int((dis - dis % 10) / 10)
        dis2 = dis % 10
        dis1_path = f'pic/distance/路程{dis1}.jpg'
        dis2_path = f'pic/distance/路程{dis2}.jpg'
        dis1_image = Image.open(dis1_path)
        dis2_image = Image.open(dis2_path)
        if body_id == 1:
            dis1_xy = (self.disxy[0][0], self.disxy[0][1] - 1)
            body_image_copy.paste(dis1_image, dis1_xy)
        else:
            body_image_copy.paste(dis1_image, self.disxy[0])
        body_image_copy.paste(dis2_image, self.disxy[1])

        spe = int(tb_data[1])
        spe1 = int((spe - spe % 100) / 100)
        spe2 = int((spe % 100 - spe % 10) / 10)
        spe3 = spe % 10
        spe1_path = f'pic/detail/数据{spe1}.jpg'
        spe2_path = f'pic/detail/数据{spe2}.jpg'
        spe3_path = f'pic/detail/数据{spe3}.jpg'
        spe1_image = Image.open(spe1_path)
        spe2_image = Image.open(spe2_path)
        spe3_image = Image.open(spe3_path)
        body_image_copy.paste(spe1_image, self.detailxy[0])
        body_image_copy.paste(spe2_image, self.detailxy[1])
        body_image_copy.paste(spe3_image, self.detailxy[2])

        tim = int(tb_data[2])
        tim1 = int((tim - tim % 100) / 100)
        tim2 = int((tim % 100 - tim % 10) / 10)
        tim3 = tim % 10
        tim1_path = f'pic/detail/数据{tim1}.jpg'
        tim2_path = f'pic/detail/数据{tim2}.jpg'
        tim3_path = f'pic/detail/数据{tim3}.jpg'
        tim1_image = Image.open(tim1_path)
        tim2_image = Image.open(tim2_path)
        tim3_image = Image.open(tim3_path)
        body_image_copy.paste(tim1_image, self.detailxy[3])
        body_image_copy.paste(tim2_image, self.detailxy[4])
        body_image_copy.paste(tim3_image, self.detailxy[5])

        year = int(day[0]) % 10
        month = int(day[1])
        month1 = int((month - month % 10) / 10)
        month2 = month % 10
        date = int(day[2])
        date1 = int((date - date % 10) / 10)
        date2 = date % 10
        year_path = f'pic/circumstances/时间{year}.jpg'
        month1_path = f'pic/circumstances/时间{month1}.jpg'
        month2_path = f'pic/circumstances/时间{month2}.jpg'
        date1_path = f'pic/circumstances/时间{date1}.jpg'
        date2_path = f'pic/circumstances/时间{date2}.jpg'
        year_image = Image.open(year_path)
        month1_image = Image.open(month1_path)
        month2_image = Image.open(month2_path)
        date1_image = Image.open(date1_path)
        date2_image = Image.open(date2_path)
        body_image_copy.paste(year_image, self.timexy[0])
        body_image_copy.paste(month1_image, self.timexy[1])
        body_image_copy.paste(month2_image, self.timexy[2])
        body_image_copy.paste(date1_image, self.timexy[3])
        body_image_copy.paste(date2_image, self.timexy[4])

        return body_image_copy

    def edit_pics(self, tb_datas, days, file_path):
        dates = get_between_day_list(days)
        for i in range(len(dates)):
            image = self.edit_pic(tb_datas[i], dates[i])
            image.save(file_path + '\\' + dates[i][0] + dates[i][1] + dates[i][2] + '.jpg')
