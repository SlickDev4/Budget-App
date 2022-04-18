import sqlite3
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from testdb import DataBase

global jan_res, feb_res, mar_res, apr_res, may_res, jun_res, jul_res, aug_res, sep_res, oct_res, nov_res, dec_res


# General functions related to all screens
# Conditions
def empty_fields_cond(self):
    if self.ids.rent_input.text == "":
        self.ids.rent_input.text = "0"
    if self.ids.electricity_input.text == "":
        self.ids.electricity_input.text = "0"
    if self.ids.heat_input.text == "":
        self.ids.heat_input.text = "0"
    if self.ids.water_input.text == "":
        self.ids.water_input.text = "0"
    if self.ids.food_input.text == "":
        self.ids.food_input.text = "0"
    if self.ids.building_input.text == "":
        self.ids.building_input.text = "0"
    if self.ids.internet_input.text == "":
        self.ids.internet_input.text = "0"
    if self.ids.goofy_input.text == "":
        self.ids.goofy_input.text = "0"
    if self.ids.cigarettes_input.text == "":
        self.ids.cigarettes_input.text = "0"
    if self.ids.credit_input.text == "":
        self.ids.credit_input.text = "0"
    if self.ids.additional_input.text == "":
        self.ids.additional_input.text = "0"


def delete_cond(self):
    if not self.ids.confirm_delete_1.active or not self.ids.confirm_delete_2.active \
            or not self.ids.confirm_delete_3.active or not self.ids.confirm_delete_4.active:
        self.ids.delete.disabled = True
    else:
        self.ids.delete.disabled = False


def delete_cond_reset(self):
    self.ids.confirm_delete_1.active = False
    self.ids.confirm_delete_2.active = False
    self.ids.confirm_delete_3.active = False
    self.ids.confirm_delete_4.active = False


# Buttons
def hide(self):
    def add_widgets_disable():
        self.ids.plus.opacity = 0
        self.ids.rent_add.opacity = 0
        self.ids.electricity_add.opacity = 0
        self.ids.heat_add.opacity = 0
        self.ids.water_add.opacity = 0
        self.ids.food_add.opacity = 0
        self.ids.building_add.opacity = 0
        self.ids.internet_add.opacity = 0
        self.ids.goofy_add.opacity = 0
        self.ids.cigarettes_add.opacity = 0
        self.ids.credit_add.opacity = 0
        self.ids.additional_add.opacity = 0
        self.ids.add_equal.opacity = 0

        self.ids.rent_add.disabled = True
        self.ids.electricity_add.disabled = True
        self.ids.heat_add.disabled = True
        self.ids.water_add.disabled = True
        self.ids.food_add.disabled = True
        self.ids.building_add.disabled = True
        self.ids.internet_add.disabled = True
        self.ids.goofy_add.disabled = True
        self.ids.cigarettes_add.disabled = True
        self.ids.credit_add.disabled = True
        self.ids.additional_add.disabled = True
        self.ids.add_equal.disabled = True

    def checkbox_disable():
        self.ids.rent_check.opacity = 0
        self.ids.electricity_check.opacity = 0
        self.ids.heat_check.opacity = 0
        self.ids.water_check.opacity = 0
        self.ids.food_check.opacity = 0
        self.ids.building_check.opacity = 0
        self.ids.internet_check.opacity = 0
        self.ids.goofy_check.opacity = 0
        self.ids.cigarettes_check.opacity = 0
        self.ids.credit_check.opacity = 0
        self.ids.additional_check.opacity = 0

        self.ids.rent_check.disabled = True
        self.ids.electricity_check.disabled = True
        self.ids.heat_check.disabled = True
        self.ids.water_check.disabled = True
        self.ids.food_check.disabled = True
        self.ids.building_check.disabled = True
        self.ids.internet_check.disabled = True
        self.ids.goofy_check.disabled = True
        self.ids.cigarettes_check.disabled = True
        self.ids.credit_check.disabled = True
        self.ids.additional_check.disabled = True

    def mini_disable():
        self.ids.rent_paid.opacity = 0
        self.ids.electricity_paid.opacity = 0
        self.ids.heat_paid.opacity = 0
        self.ids.water_paid.opacity = 0
        self.ids.food_paid.opacity = 0
        self.ids.building_paid.opacity = 0
        self.ids.internet_paid.opacity = 0
        self.ids.goofy_paid.opacity = 0
        self.ids.cigarettes_paid.opacity = 0
        self.ids.credit_paid.opacity = 0
        self.ids.additional_paid.opacity = 0

        self.ids.rent_unpaid.opacity = 0
        self.ids.electricity_unpaid.opacity = 0
        self.ids.heat_unpaid.opacity = 0
        self.ids.water_unpaid.opacity = 0
        self.ids.food_unpaid.opacity = 0
        self.ids.building_unpaid.opacity = 0
        self.ids.internet_unpaid.opacity = 0
        self.ids.goofy_unpaid.opacity = 0
        self.ids.cigarettes_unpaid.opacity = 0
        self.ids.credit_unpaid.opacity = 0
        self.ids.additional_unpaid.opacity = 0

    def table_disable():
        self.ids.table_1.opacity = 0
        self.ids.table_2.opacity = 0
        self.ids.table_3.opacity = 0
        self.ids.table_4.opacity = 0
        self.ids.table_5.opacity = 0
        self.ids.table_6.opacity = 0
        self.ids.table_7.opacity = 0
        self.ids.table_8.opacity = 0
        self.ids.table_9.opacity = 0
        self.ids.table_10.opacity = 0
        self.ids.table_11.opacity = 0
        self.ids.table_12.opacity = 0
        self.ids.table_13.opacity = 0
        self.ids.table_14.opacity = 0
        self.ids.table_15.opacity = 0
        self.ids.table_16.opacity = 0
        self.ids.table_17.opacity = 0
        self.ids.table_18.opacity = 0

    def main_disable():
        self.ids.show_total_paid_1.text = ""
        self.ids.show_total_paid_2.text = ""
        self.ids.show_total_paid_3.text = ""
        self.ids.show_total_paid_4.text = ""

        self.ids.rent_label.text = ""
        self.ids.electricity_label.text = ""
        self.ids.heat_label.text = ""
        self.ids.water_label.text = ""
        self.ids.food_label.text = ""
        self.ids.building_label.text = ""
        self.ids.internet_label.text = ""
        self.ids.goofy_label.text = ""
        self.ids.cigarettes_label.text = ""
        self.ids.credit_label.text = ""
        self.ids.additional_label.text = ""

        self.ids.rent_price.text = ""
        self.ids.electricity_price.text = ""
        self.ids.heat_price.text = ""
        self.ids.water_price.text = ""
        self.ids.food_price.text = ""
        self.ids.building_price.text = ""
        self.ids.internet_price.text = ""
        self.ids.goofy_price.text = ""
        self.ids.cigarettes_price.text = ""
        self.ids.credit_price.text = ""
        self.ids.additional_price.text = ""

        self.ids.show_boxes_labels.opacity = 0
        self.ids.show_total_paid_1.opacity = 0
        self.ids.show_total_paid_2.opacity = 0
        self.ids.show_total_paid_3.opacity = 0
        self.ids.show_total_paid_4.opacity = 0

        self.ids.rent_label.opacity = 0
        self.ids.electricity_label.opacity = 0
        self.ids.heat_label.opacity = 0
        self.ids.water_label.opacity = 0
        self.ids.food_label.opacity = 0
        self.ids.building_label.opacity = 0
        self.ids.internet_label.opacity = 0
        self.ids.goofy_label.opacity = 0
        self.ids.cigarettes_label.opacity = 0
        self.ids.credit_label.opacity = 0
        self.ids.additional_label.opacity = 0

        self.ids.rent_price.opacity = 0
        self.ids.electricity_price.opacity = 0
        self.ids.heat_price.opacity = 0
        self.ids.water_price.opacity = 0
        self.ids.food_price.opacity = 0
        self.ids.building_price.opacity = 0
        self.ids.internet_price.opacity = 0
        self.ids.goofy_price.opacity = 0
        self.ids.cigarettes_price.opacity = 0
        self.ids.credit_price.opacity = 0
        self.ids.additional_price.opacity = 0

    add_widgets_disable()
    checkbox_disable()
    mini_disable()
    table_disable()
    main_disable()


def cancel(self):
    self.ids.rent_input.text = ''
    self.ids.electricity_input.text = ''
    self.ids.heat_input.text = ''
    self.ids.water_input.text = ''
    self.ids.food_input.text = ''
    self.ids.building_input.text = ''
    self.ids.internet_input.text = ''
    self.ids.goofy_input.text = ''
    self.ids.cigarettes_input.text = ''
    self.ids.credit_input.text = ''
    self.ids.additional_input.text = ''

    self.ids.rent_add.text = ''
    self.ids.electricity_add.text = ''
    self.ids.heat_add.text = ''
    self.ids.water_add.text = ''
    self.ids.food_add.text = ''
    self.ids.building_add.text = ''
    self.ids.internet_add.text = ''
    self.ids.goofy_add.text = ''
    self.ids.cigarettes_add.text = ''
    self.ids.credit_add.text = ''
    self.ids.additional_add.text = ''

    self.ids.show.text = "Show Table"
    self.ids.save.disabled = True


# Enable, Paid/Unpaid, Calculator and Uncheck on Delete Functions
def widgets_enable(self):
    def checkbox_enable():
        self.ids.rent_check.opacity = 1
        self.ids.electricity_check.opacity = 1
        self.ids.heat_check.opacity = 1
        self.ids.water_check.opacity = 1
        self.ids.food_check.opacity = 1
        self.ids.building_check.opacity = 1
        self.ids.internet_check.opacity = 1
        self.ids.goofy_check.opacity = 1
        self.ids.cigarettes_check.opacity = 1
        self.ids.credit_check.opacity = 1
        self.ids.additional_check.opacity = 1

        self.ids.rent_check.disabled = False
        self.ids.electricity_check.disabled = False
        self.ids.heat_check.disabled = False
        self.ids.water_check.disabled = False
        self.ids.food_check.disabled = False
        self.ids.building_check.disabled = False
        self.ids.internet_check.disabled = False
        self.ids.goofy_check.disabled = False
        self.ids.cigarettes_check.disabled = False
        self.ids.credit_check.disabled = False
        self.ids.additional_check.disabled = False

    def table_enable():
        self.ids.table_1.opacity = 1
        self.ids.table_2.opacity = 1
        self.ids.table_3.opacity = 1
        self.ids.table_4.opacity = 1
        self.ids.table_5.opacity = 1
        self.ids.table_6.opacity = 1
        self.ids.table_7.opacity = 1
        self.ids.table_8.opacity = 1
        self.ids.table_9.opacity = 1
        self.ids.table_10.opacity = 1
        self.ids.table_11.opacity = 1
        self.ids.table_12.opacity = 1
        self.ids.table_13.opacity = 1
        self.ids.table_14.opacity = 1
        self.ids.table_15.opacity = 1
        self.ids.table_16.opacity = 1
        self.ids.table_17.opacity = 1
        self.ids.table_18.opacity = 1

    def main_enable():
        self.ids.show_boxes_labels.opacity = 1
        self.ids.show_total_paid_1.opacity = 1
        self.ids.show_total_paid_2.opacity = 1
        self.ids.show_total_paid_3.opacity = 1
        self.ids.show_total_paid_4.opacity = 1

        self.ids.rent_label.opacity = 1
        self.ids.electricity_label.opacity = 1
        self.ids.heat_label.opacity = 1
        self.ids.water_label.opacity = 1
        self.ids.food_label.opacity = 1
        self.ids.building_label.opacity = 1
        self.ids.internet_label.opacity = 1
        self.ids.goofy_label.opacity = 1
        self.ids.cigarettes_label.opacity = 1
        self.ids.credit_label.opacity = 1
        self.ids.additional_label.opacity = 1

        self.ids.rent_price.opacity = 1
        self.ids.electricity_price.opacity = 1
        self.ids.heat_price.opacity = 1
        self.ids.water_price.opacity = 1
        self.ids.food_price.opacity = 1
        self.ids.building_price.opacity = 1
        self.ids.internet_price.opacity = 1
        self.ids.goofy_price.opacity = 1
        self.ids.cigarettes_price.opacity = 1
        self.ids.credit_price.opacity = 1
        self.ids.additional_price.opacity = 1

    checkbox_enable()
    table_enable()
    main_enable()


def add_widgets_enable(self):
    self.ids.plus.opacity = 1
    self.ids.rent_add.opacity = 1
    self.ids.electricity_add.opacity = 1
    self.ids.heat_add.opacity = 1
    self.ids.water_add.opacity = 1
    self.ids.food_add.opacity = 1
    self.ids.building_add.opacity = 1
    self.ids.internet_add.opacity = 1
    self.ids.goofy_add.opacity = 1
    self.ids.cigarettes_add.opacity = 1
    self.ids.credit_add.opacity = 1
    self.ids.additional_add.opacity = 1
    self.ids.add_equal.opacity = 1

    self.ids.rent_add.disabled = False
    self.ids.electricity_add.disabled = False
    self.ids.heat_add.disabled = False
    self.ids.water_add.disabled = False
    self.ids.food_add.disabled = False
    self.ids.building_add.disabled = False
    self.ids.internet_add.disabled = False
    self.ids.goofy_add.disabled = False
    self.ids.cigarettes_add.disabled = False
    self.ids.credit_add.disabled = False
    self.ids.additional_add.disabled = False
    self.ids.add_equal.disabled = False
    self.ids.save.disabled = False


def show_paid_unpaid(self):
    def show_paid():
        if int(self.ids.rent_check.active) == 0:
            self.ids.rent_paid.opacity = 0
        else:
            self.ids.rent_paid.opacity = 1
            self.ids.rent_paid.text = 'Paid!'
            self.ids.rent_paid.background_color = (0, 1, 0, 1)

        if int(self.ids.electricity_check.active) == 0:
            self.ids.electricity_paid.opacity = 0
        else:
            self.ids.electricity_paid.opacity = 1
            self.ids.electricity_paid.text = 'Paid!'
            self.ids.electricity_paid.background_color = (0, 1, 0, 1)

        if int(self.ids.heat_check.active) == 0:
            self.ids.heat_paid.opacity = 0
        else:
            self.ids.heat_paid.opacity = 1
            self.ids.heat_paid.text = 'Paid!'
            self.ids.heat_paid.background_color = (0, 1, 0, 1)

        if int(self.ids.water_check.active) == 0:
            self.ids.water_paid.opacity = 0
        else:
            self.ids.water_paid.opacity = 1
            self.ids.water_paid.text = 'Paid!'
            self.ids.water_paid.background_color = (0, 1, 0, 1)

        if int(self.ids.food_check.active) == 0:
            self.ids.food_paid.opacity = 0
        else:
            self.ids.food_paid.opacity = 1
            self.ids.food_paid.text = 'Paid!'
            self.ids.food_paid.background_color = (0, 1, 0, 1)

        if int(self.ids.building_check.active) == 0:
            self.ids.building_paid.opacity = 0
        else:
            self.ids.building_paid.opacity = 1
            self.ids.building_paid.text = 'Paid!'
            self.ids.building_paid.background_color = (0, 1, 0, 1)

        if int(self.ids.internet_check.active) == 0:
            self.ids.internet_paid.opacity = 0
        else:
            self.ids.internet_paid.opacity = 1
            self.ids.internet_paid.text = 'Paid!'
            self.ids.internet_paid.background_color = (0, 1, 0, 1)

        if int(self.ids.goofy_check.active) == 0:
            self.ids.goofy_paid.opacity = 0
        else:
            self.ids.goofy_paid.opacity = 1
            self.ids.goofy_paid.text = 'Paid!'
            self.ids.goofy_paid.background_color = (0, 1, 0, 1)

        if int(self.ids.cigarettes_check.active) == 0:
            self.ids.cigarettes_paid.opacity = 0
        else:
            self.ids.cigarettes_paid.opacity = 1
            self.ids.cigarettes_paid.text = 'Paid!'
            self.ids.cigarettes_paid.background_color = (0, 1, 0, 1)

        if int(self.ids.credit_check.active) == 0:
            self.ids.credit_paid.opacity = 0
        else:
            self.ids.credit_paid.opacity = 1
            self.ids.credit_paid.text = 'Paid!'
            self.ids.credit_paid.background_color = (0, 1, 0, 1)

        if int(self.ids.additional_check.active) == 0:
            self.ids.additional_paid.opacity = 0
        else:
            self.ids.additional_paid.opacity = 1
            self.ids.additional_paid.text = 'Paid!'
            self.ids.additional_paid.background_color = (0, 1, 0, 1)

    def show_unpaid():
        if int(self.ids.rent_check.active) == 1:
            self.ids.rent_unpaid.opacity = 0
        else:
            self.ids.rent_unpaid.opacity = 1
            self.ids.rent_unpaid.text = 'Unpaid!'
            self.ids.rent_unpaid.background_color = (1, 0, 0, 1)

        if int(self.ids.electricity_check.active) == 1:
            self.ids.electricity_unpaid.opacity = 0
        else:
            self.ids.electricity_unpaid.opacity = 1
            self.ids.electricity_unpaid.text = 'Unpaid!'
            self.ids.electricity_unpaid.background_color = (1, 0, 0, 1)

        if int(self.ids.heat_check.active) == 1:
            self.ids.heat_unpaid.opacity = 0
        else:
            self.ids.heat_unpaid.opacity = 1
            self.ids.heat_unpaid.text = 'Unpaid!'
            self.ids.heat_unpaid.background_color = (1, 0, 0, 1)

        if int(self.ids.water_check.active) == 1:
            self.ids.water_unpaid.opacity = 0
        else:
            self.ids.water_unpaid.opacity = 1
            self.ids.water_unpaid.text = 'Unpaid!'
            self.ids.water_unpaid.background_color = (1, 0, 0, 1)

        if int(self.ids.food_check.active) == 1:
            self.ids.food_unpaid.opacity = 0
        else:
            self.ids.food_unpaid.opacity = 1
            self.ids.food_unpaid.text = 'Unpaid!'
            self.ids.food_unpaid.background_color = (1, 0, 0, 1)

        if int(self.ids.building_check.active) == 1:
            self.ids.building_unpaid.opacity = 0
        else:
            self.ids.building_unpaid.opacity = 1
            self.ids.building_unpaid.text = 'Unpaid!'
            self.ids.building_unpaid.background_color = (1, 0, 0, 1)

        if int(self.ids.internet_check.active) == 1:
            self.ids.internet_unpaid.opacity = 0
        else:
            self.ids.internet_unpaid.opacity = 1
            self.ids.internet_unpaid.text = 'Unpaid!'
            self.ids.internet_unpaid.background_color = (1, 0, 0, 1)

        if int(self.ids.goofy_check.active) == 1:
            self.ids.goofy_unpaid.opacity = 0
        else:
            self.ids.goofy_unpaid.opacity = 1
            self.ids.goofy_unpaid.text = 'Unpaid!'
            self.ids.goofy_unpaid.background_color = (1, 0, 0, 1)

        if int(self.ids.cigarettes_check.active) == 1:
            self.ids.cigarettes_unpaid.opacity = 0
        else:
            self.ids.cigarettes_unpaid.opacity = 1
            self.ids.cigarettes_unpaid.text = 'Unpaid!'
            self.ids.cigarettes_unpaid.background_color = (1, 0, 0, 1)

        if int(self.ids.credit_check.active) == 1:
            self.ids.credit_unpaid.opacity = 0
        else:
            self.ids.credit_unpaid.opacity = 1
            self.ids.credit_unpaid.text = 'Unpaid!'
            self.ids.credit_unpaid.background_color = (1, 0, 0, 1)

        if int(self.ids.additional_check.active) == 1:
            self.ids.additional_unpaid.opacity = 0
        else:
            self.ids.additional_unpaid.opacity = 1
            self.ids.additional_unpaid.text = 'Unpaid!'
            self.ids.additional_unpaid.background_color = (1, 0, 0, 1)

    show_paid()
    show_unpaid()


def add_function(self):
    def add_rent():
        if self.ids.rent_input.text == "":
            rent = 0
        else:
            rent = int(self.ids.rent_input.text)

        if self.ids.rent_add.text == "":
            add = 0
        else:
            add = int(self.ids.rent_add.text)

        res = rent + add
        self.ids.rent_input.text = ""
        self.ids.rent_add.text = ""
        self.ids.rent_input.text = str(res)

    def add_electricity():
        if self.ids.electricity_input.text == "":
            electricity = 0
        else:
            electricity = int(self.ids.electricity_input.text)

        if self.ids.electricity_add.text == "":
            add = 0
        else:
            add = int(self.ids.electricity_add.text)

        res = electricity + add
        self.ids.electricity_input.text = ""
        self.ids.electricity_add.text = ""
        self.ids.electricity_input.text = str(res)

    def add_heat():
        if self.ids.heat_input.text == "":
            heat = 0
        else:
            heat = int(self.ids.heat_input.text)

        if self.ids.heat_add.text == "":
            add = 0
        else:
            add = int(self.ids.heat_add.text)

        res = heat + add
        self.ids.heat_input.text = ""
        self.ids.heat_add.text = ""
        self.ids.heat_input.text = str(res)

    def add_water():
        if self.ids.water_input.text == "":
            water = 0
        else:
            water = int(self.ids.water_input.text)

        if self.ids.water_add.text == "":
            add = 0
        else:
            add = int(self.ids.water_add.text)

        res = water + add
        self.ids.water_input.text = ""
        self.ids.water_add.text = ""
        self.ids.water_input.text = str(res)

    def add_food():
        if self.ids.food_input.text == "":
            food = 0
        else:
            food = int(self.ids.food_input.text)

        if self.ids.food_add.text == "":
            add = 0
        else:
            add = int(self.ids.food_add.text)

        res = food + add
        self.ids.food_input.text = ""
        self.ids.food_add.text = ""
        self.ids.food_input.text = str(res)

    def add_building():
        if self.ids.building_input.text == "":
            building = 0
        else:
            building = int(self.ids.building_input.text)

        if self.ids.building_add.text == "":
            add = 0
        else:
            add = int(self.ids.building_add.text)

        res = building + add
        self.ids.building_input.text = ""
        self.ids.building_add.text = ""
        self.ids.building_input.text = str(res)

    def add_internet():
        if self.ids.internet_input.text == "":
            internet = 0
        else:
            internet = int(self.ids.internet_input.text)

        if self.ids.internet_add.text == "":
            add = 0
        else:
            add = int(self.ids.internet_add.text)

        res = internet + add
        self.ids.internet_input.text = ""
        self.ids.internet_add.text = ""
        self.ids.internet_input.text = str(res)

    def add_goofy():
        if self.ids.goofy_input.text == "":
            goofy = 0
        else:
            goofy = int(self.ids.goofy_input.text)

        if self.ids.goofy_add.text == "":
            add = 0
        else:
            add = int(self.ids.goofy_add.text)

        res = goofy + add
        self.ids.goofy_input.text = ""
        self.ids.goofy_add.text = ""
        self.ids.goofy_input.text = str(res)

    def add_cigarettes():
        if self.ids.cigarettes_input.text == "":
            cigarettes = 0
        else:
            cigarettes = int(self.ids.cigarettes_input.text)

        if self.ids.cigarettes_add.text == "":
            add = 0
        else:
            add = int(self.ids.cigarettes_add.text)

        res = cigarettes + add
        self.ids.cigarettes_input.text = ""
        self.ids.cigarettes_add.text = ""
        self.ids.cigarettes_input.text = str(res)

    def add_credit():
        if self.ids.credit_input.text == "":
            credit = 0
        else:
            credit = int(self.ids.credit_input.text)

        if self.ids.credit_add.text == "":
            add = 0
        else:
            add = int(self.ids.credit_add.text)

        res = credit + add
        self.ids.credit_input.text = ""
        self.ids.credit_add.text = ""
        self.ids.credit_input.text = str(res)

    def add_additional():
        if self.ids.additional_input.text == "":
            additional = 0
        else:
            additional = int(self.ids.additional_input.text)

        if self.ids.additional_add.text == "":
            add = 0
        else:
            add = int(self.ids.additional_add.text)

        res = additional + add
        self.ids.additional_input.text = ""
        self.ids.additional_add.text = ""
        self.ids.additional_input.text = str(res)

    add_rent()
    add_electricity()
    add_heat()
    add_water()
    add_food()
    add_building()
    add_internet()
    add_goofy()
    add_cigarettes()
    add_credit()
    add_additional()


def uncheck(self):
    self.ids.rent_check.active = False
    self.ids.electricity_check.active = False
    self.ids.heat_check.active = False
    self.ids.water_check.active = False
    self.ids.food_check.active = False
    self.ids.building_check.active = False
    self.ids.internet_check.active = False
    self.ids.goofy_check.active = False
    self.ids.cigarettes_check.active = False
    self.ids.credit_check.active = False
    self.ids.additional_check.active = False


# Rename Buttons and related Functions
def rename(self):
    def input_text():
        self.ids.rent_input.input_filter = None
        self.ids.electricity_input.input_filter = None
        self.ids.heat_input.input_filter = None
        self.ids.water_input.input_filter = None
        self.ids.food_input.input_filter = None
        self.ids.building_input.input_filter = None
        self.ids.internet_input.input_filter = None
        self.ids.goofy_input.input_filter = None
        self.ids.cigarettes_input.input_filter = None
        self.ids.credit_input.input_filter = None
        self.ids.additional_input.input_filter = None

    def fields():
        self.ids.rent_input.text = self.ids.rent_rename.text
        self.ids.electricity_input.text = self.ids.electricity_rename.text
        self.ids.heat_input.text = self.ids.heat_rename.text
        self.ids.water_input.text = self.ids.water_rename.text
        self.ids.food_input.text = self.ids.food_rename.text
        self.ids.building_input.text = self.ids.building_rename.text
        self.ids.internet_input.text = self.ids.internet_rename.text
        self.ids.goofy_input.text = self.ids.goofy_rename.text
        self.ids.cigarettes_input.text = self.ids.cigarettes_rename.text
        self.ids.credit_input.text = self.ids.credit_rename.text
        self.ids.additional_input.text = self.ids.additional_rename.text

    def disable_other():
        self.ids.submit.disabled = True
        self.ids.edit.disabled = True
        self.ids.save.disabled = True
        self.ids.cancel.disabled = True
        self.ids.show.disabled = True
        self.ids.rename.disabled = True

        self.ids.confirm_delete_1.disabled = True
        self.ids.confirm_delete_2.disabled = True
        self.ids.confirm_delete_3.disabled = True
        self.ids.confirm_delete_4.disabled = True

        self.ids.save_rename.disabled = False
        self.ids.confirm_delete_1.active = False

    input_text()
    fields()
    disable_other()


def input_numbers(self):
    self.ids.rent_input.input_filter = 'int'
    self.ids.electricity_input.input_filter = 'int'
    self.ids.heat_input.input_filter = 'int'
    self.ids.water_input.input_filter = 'int'
    self.ids.food_input.input_filter = 'int'
    self.ids.building_input.input_filter = 'int'
    self.ids.internet_input.input_filter = 'int'
    self.ids.goofy_input.input_filter = 'int'
    self.ids.cigarettes_input.input_filter = 'int'
    self.ids.credit_input.input_filter = 'int'
    self.ids.additional_input.input_filter = 'int'


def enable_other(self):
    self.ids.edit.disabled = False
    self.ids.cancel.disabled = False
    self.ids.show.disabled = False
    self.ids.rename.disabled = False

    self.ids.confirm_delete_1.disabled = False
    self.ids.confirm_delete_2.disabled = False
    self.ids.confirm_delete_3.disabled = False
    self.ids.confirm_delete_4.disabled = False

    self.ids.save_rename.disabled = True
    self.ids.submit.disabled = True
    self.ids.save.disabled = True


def save_rename(self):
    def actual_rename():
        self.ids.rent_rename.text = self.ids.rent_input.text.capitalize()
        self.ids.electricity_rename.text = self.ids.electricity_input.text.capitalize()
        self.ids.heat_rename.text = self.ids.heat_input.text.capitalize()
        self.ids.water_rename.text = self.ids.water_input.text.capitalize()
        self.ids.food_rename.text = self.ids.food_input.text.capitalize()
        self.ids.building_rename.text = self.ids.building_input.text.capitalize()
        self.ids.internet_rename.text = self.ids.internet_input.text.capitalize()
        self.ids.goofy_rename.text = self.ids.goofy_input.text.capitalize()
        self.ids.cigarettes_rename.text = self.ids.cigarettes_input.text.capitalize()
        self.ids.credit_rename.text = self.ids.credit_input.text.capitalize()
        self.ids.additional_rename.text = self.ids.additional_input.text.capitalize()

    def clear_fields():
        self.ids.rent_input.text = ""
        self.ids.electricity_input.text = ""
        self.ids.heat_input.text = ""
        self.ids.water_input.text = ""
        self.ids.food_input.text = ""
        self.ids.building_input.text = ""
        self.ids.internet_input.text = ""
        self.ids.goofy_input.text = ""
        self.ids.cigarettes_input.text = ""
        self.ids.credit_input.text = ""
        self.ids.additional_input.text = ""

    def input_length():
        self.ids.rent_input.text = self.ids.rent_input.text[0:15]
        self.ids.electricity_input.text = self.ids.electricity_input.text[0:15]
        self.ids.heat_input.text = self.ids.heat_input.text[0:15]
        self.ids.water_input.text = self.ids.water_input.text[0:15]
        self.ids.food_input.text = self.ids.food_input.text[0:15]
        self.ids.building_input.text = self.ids.building_input.text[0:15]
        self.ids.internet_input.text = self.ids.internet_input.text[0:15]
        self.ids.goofy_input.text = self.ids.goofy_input.text[0:15]
        self.ids.cigarettes_input.text = self.ids.cigarettes_input.text[0:15]
        self.ids.credit_input.text = self.ids.credit_input.text[0:15]
        self.ids.additional_input.text = self.ids.additional_input.text[0:15]

    input_length()
    actual_rename()
    save_rename_config()
    clear_fields()
    input_numbers(self)
    enable_other(self)


def show_rename_in_table(self):
    self.ids.rent_label.text = self.ids.rent_rename.text
    self.ids.electricity_label.text = self.ids.electricity_rename.text
    self.ids.heat_label.text = self.ids.heat_rename.text
    self.ids.water_label.text = self.ids.water_rename.text
    self.ids.food_label.text = self.ids.food_rename.text
    self.ids.building_label.text = self.ids.building_rename.text
    self.ids.internet_label.text = self.ids.internet_rename.text
    self.ids.goofy_label.text = self.ids.goofy_rename.text
    self.ids.cigarettes_label.text = self.ids.cigarettes_rename.text
    self.ids.credit_label.text = self.ids.credit_rename.text
    self.ids.additional_label.text = self.ids.additional_rename.text


def remove_text_on_click_rename(self):
    def rent():
        if not self.ids.save_rename.disabled:
            if self.ids.rent_input.focus:
                self.ids.rent_input.text = ''
            if not self.ids.rent_input.focus:
                if self.ids.rent_input.text == '':
                    self.ids.rent_input.text = self.ids.rent_rename.text

    def electricity():
        if not self.ids.save_rename.disabled:
            if self.ids.electricity_input.focus:
                self.ids.electricity_input.text = ''
            if not self.ids.electricity_input.focus:
                if self.ids.electricity_input.text == '':
                    self.ids.electricity_input.text = self.ids.electricity_rename.text

    def heat():
        if not self.ids.save_rename.disabled:
            if self.ids.heat_input.focus:
                self.ids.heat_input.text = ''
            if not self.ids.heat_input.focus:
                if self.ids.heat_input.text == '':
                    self.ids.heat_input.text = self.ids.heat_rename.text

    def water():
        if not self.ids.save_rename.disabled:
            if self.ids.water_input.focus:
                self.ids.water_input.text = ''
            if not self.ids.water_input.focus:
                if self.ids.water_input.text == '':
                    self.ids.water_input.text = self.ids.water_rename.text

    def food():
        if not self.ids.save_rename.disabled:
            if self.ids.food_input.focus:
                self.ids.food_input.text = ''
            if not self.ids.food_input.focus:
                if self.ids.food_input.text == '':
                    self.ids.food_input.text = self.ids.food_rename.text

    def building():
        if not self.ids.save_rename.disabled:
            if self.ids.building_input.focus:
                self.ids.building_input.text = ''
            if not self.ids.building_input.focus:
                if self.ids.building_input.text == '':
                    self.ids.building_input.text = self.ids.building_rename.text

    def internet():
        if not self.ids.save_rename.disabled:
            if self.ids.internet_input.focus:
                self.ids.internet_input.text = ''
            if not self.ids.internet_input.focus:
                if self.ids.internet_input.text == '':
                    self.ids.internet_input.text = self.ids.internet_rename.text

    def goofy():
        if not self.ids.save_rename.disabled:
            if self.ids.goofy_input.focus:
                self.ids.goofy_input.text = ''
            if not self.ids.goofy_input.focus:
                if self.ids.goofy_input.text == '':
                    self.ids.goofy_input.text = self.ids.goofy_rename.text

    def cigarettes():
        if not self.ids.save_rename.disabled:
            if self.ids.cigarettes_input.focus:
                self.ids.cigarettes_input.text = ''
            if not self.ids.cigarettes_input.focus:
                if self.ids.cigarettes_input.text == '':
                    self.ids.cigarettes_input.text = self.ids.cigarettes_rename.text

    def credit():
        if not self.ids.save_rename.disabled:
            if self.ids.credit_input.focus:
                self.ids.credit_input.text = ''
            if not self.ids.credit_input.focus:
                if self.ids.credit_input.text == '':
                    self.ids.credit_input.text = self.ids.credit_rename.text

    def additional():
        if not self.ids.save_rename.disabled:
            if self.ids.additional_input.focus:
                self.ids.additional_input.text = ''
            if not self.ids.additional_input.focus:
                if self.ids.additional_input.text == '':
                    self.ids.additional_input.text = self.ids.additional_rename.text

    rent()
    electricity()
    heat()
    water()
    food()
    building()
    internet()
    goofy()
    cigarettes()
    credit()
    additional()


# Saving Rename details and Reloading the same Config on Application Restart
def save_rename_config():
    r1 = screens[3].ids.rent_rename.text
    e1 = screens[3].ids.electricity_rename.text
    h1 = screens[3].ids.heat_rename.text
    w1 = screens[3].ids.water_rename.text
    f1 = screens[3].ids.food_rename.text
    b1 = screens[3].ids.building_rename.text
    i1 = screens[3].ids.internet_rename.text
    g1 = screens[3].ids.goofy_rename.text
    ci1 = screens[3].ids.cigarettes_rename.text
    cr1 = screens[3].ids.credit_rename.text
    a1 = screens[3].ids.additional_rename.text

    r2 = screens[4].ids.rent_rename.text
    e2 = screens[4].ids.electricity_rename.text
    h2 = screens[4].ids.heat_rename.text
    w2 = screens[4].ids.water_rename.text
    f2 = screens[4].ids.food_rename.text
    b2 = screens[4].ids.building_rename.text
    i2 = screens[4].ids.internet_rename.text
    g2 = screens[4].ids.goofy_rename.text
    ci2 = screens[4].ids.cigarettes_rename.text
    cr2 = screens[4].ids.credit_rename.text
    a2 = screens[4].ids.additional_rename.text

    r3 = screens[5].ids.rent_rename.text
    e3 = screens[5].ids.electricity_rename.text
    h3 = screens[5].ids.heat_rename.text
    w3 = screens[5].ids.water_rename.text
    f3 = screens[5].ids.food_rename.text
    b3 = screens[5].ids.building_rename.text
    i3 = screens[5].ids.internet_rename.text
    g3 = screens[5].ids.goofy_rename.text
    ci3 = screens[5].ids.cigarettes_rename.text
    cr3 = screens[5].ids.credit_rename.text
    a3 = screens[5].ids.additional_rename.text

    r4 = screens[6].ids.rent_rename.text
    e4 = screens[6].ids.electricity_rename.text
    h4 = screens[6].ids.heat_rename.text
    w4 = screens[6].ids.water_rename.text
    f4 = screens[6].ids.food_rename.text
    b4 = screens[6].ids.building_rename.text
    i4 = screens[6].ids.internet_rename.text
    g4 = screens[6].ids.goofy_rename.text
    ci4 = screens[6].ids.cigarettes_rename.text
    cr4 = screens[6].ids.credit_rename.text
    a4 = screens[6].ids.additional_rename.text

    r5 = screens[7].ids.rent_rename.text
    e5 = screens[7].ids.electricity_rename.text
    h5 = screens[7].ids.heat_rename.text
    w5 = screens[7].ids.water_rename.text
    f5 = screens[7].ids.food_rename.text
    b5 = screens[7].ids.building_rename.text
    i5 = screens[7].ids.internet_rename.text
    g5 = screens[7].ids.goofy_rename.text
    ci5 = screens[7].ids.cigarettes_rename.text
    cr5 = screens[7].ids.credit_rename.text
    a5 = screens[7].ids.additional_rename.text

    r6 = screens[8].ids.rent_rename.text
    e6 = screens[8].ids.electricity_rename.text
    h6 = screens[8].ids.heat_rename.text
    w6 = screens[8].ids.water_rename.text
    f6 = screens[8].ids.food_rename.text
    b6 = screens[8].ids.building_rename.text
    i6 = screens[8].ids.internet_rename.text
    g6 = screens[8].ids.goofy_rename.text
    ci6 = screens[8].ids.cigarettes_rename.text
    cr6 = screens[8].ids.credit_rename.text
    a6 = screens[8].ids.additional_rename.text

    r7 = screens[9].ids.rent_rename.text
    e7 = screens[9].ids.electricity_rename.text
    h7 = screens[9].ids.heat_rename.text
    w7 = screens[9].ids.water_rename.text
    f7 = screens[9].ids.food_rename.text
    b7 = screens[9].ids.building_rename.text
    i7 = screens[9].ids.internet_rename.text
    g7 = screens[9].ids.goofy_rename.text
    ci7 = screens[9].ids.cigarettes_rename.text
    cr7 = screens[9].ids.credit_rename.text
    a7 = screens[9].ids.additional_rename.text

    r8 = screens[10].ids.rent_rename.text
    e8 = screens[10].ids.electricity_rename.text
    h8 = screens[10].ids.heat_rename.text
    w8 = screens[10].ids.water_rename.text
    f8 = screens[10].ids.food_rename.text
    b8 = screens[10].ids.building_rename.text
    i8 = screens[10].ids.internet_rename.text
    g8 = screens[10].ids.goofy_rename.text
    ci8 = screens[10].ids.cigarettes_rename.text
    cr8 = screens[10].ids.credit_rename.text
    a8 = screens[10].ids.additional_rename.text

    r9 = screens[11].ids.rent_rename.text
    e9 = screens[11].ids.electricity_rename.text
    h9 = screens[11].ids.heat_rename.text
    w9 = screens[11].ids.water_rename.text
    f9 = screens[11].ids.food_rename.text
    b9 = screens[11].ids.building_rename.text
    i9 = screens[11].ids.internet_rename.text
    g9 = screens[11].ids.goofy_rename.text
    ci9 = screens[11].ids.cigarettes_rename.text
    cr9 = screens[11].ids.credit_rename.text
    a9 = screens[11].ids.additional_rename.text

    r10 = screens[12].ids.rent_rename.text
    e10 = screens[12].ids.electricity_rename.text
    h10 = screens[12].ids.heat_rename.text
    w10 = screens[12].ids.water_rename.text
    f10 = screens[12].ids.food_rename.text
    b10 = screens[12].ids.building_rename.text
    i10 = screens[12].ids.internet_rename.text
    g10 = screens[12].ids.goofy_rename.text
    ci10 = screens[12].ids.cigarettes_rename.text
    cr10 = screens[12].ids.credit_rename.text
    a10 = screens[12].ids.additional_rename.text

    r11 = screens[13].ids.rent_rename.text
    e11 = screens[13].ids.electricity_rename.text
    h11 = screens[13].ids.heat_rename.text
    w11 = screens[13].ids.water_rename.text
    f11 = screens[13].ids.food_rename.text
    b11 = screens[13].ids.building_rename.text
    i11 = screens[13].ids.internet_rename.text
    g11 = screens[13].ids.goofy_rename.text
    ci11 = screens[13].ids.cigarettes_rename.text
    cr11 = screens[13].ids.credit_rename.text
    a11 = screens[13].ids.additional_rename.text

    r12 = screens[14].ids.rent_rename.text
    e12 = screens[14].ids.electricity_rename.text
    h12 = screens[14].ids.heat_rename.text
    w12 = screens[14].ids.water_rename.text
    f12 = screens[14].ids.food_rename.text
    b12 = screens[14].ids.building_rename.text
    i12 = screens[14].ids.internet_rename.text
    g12 = screens[14].ids.goofy_rename.text
    ci12 = screens[14].ids.cigarettes_rename.text
    cr12 = screens[14].ids.credit_rename.text
    a12 = screens[14].ids.additional_rename.text

    file = open(r"rename.txt", "w+")
    file.write(str(r1).strip() + "\n" + str(e1).strip() + "\n" + str(h1).strip() + "\n" + str(w1).strip() + "\n" +
               str(f1).strip() + "\n" + str(b1).strip() + "\n" + str(i1).strip() + "\n" + str(g1).strip() + "\n" +
               str(ci1).strip() + "\n" + str(cr1).strip() + "\n" + str(a1).strip() + "\n" + str(r2).strip() + "\n" +
               str(e2).strip() + "\n" + str(h2).strip() + "\n" + str(w2).strip() + "\n" + str(f2).strip() + "\n" +
               str(b2).strip() + "\n" + str(i2).strip() + "\n" + str(g2).strip() + "\n" + str(ci2).strip() + "\n" +
               str(cr2).strip() + "\n" + str(a2).strip() + "\n" + str(r3).strip() + "\n" + str(e3).strip() + "\n" +
               str(h3).strip() + "\n" + str(w3).strip() + "\n" + str(f3).strip() + "\n" + str(b3).strip() + "\n" +
               str(i3).strip() + "\n" + str(g3).strip() + "\n" + str(ci3).strip() + "\n" + str(cr3).strip() + "\n" +
               str(a3).strip() + "\n" + str(r4).strip() + "\n" + str(e4).strip() + "\n" + str(h4).strip() + "\n" +
               str(w4).strip() + "\n" + str(f4).strip() + "\n" + str(b4).strip() + "\n" + str(i4).strip() + "\n" +
               str(g4).strip() + "\n" + str(ci4).strip() + "\n" + str(cr4).strip() + "\n" + str(a4).strip() + "\n" +
               str(r5).strip() + "\n" + str(e5).strip() + "\n" + str(h5).strip() + "\n" + str(w5).strip() + "\n" +
               str(f5).strip() + "\n" + str(b5).strip() + "\n" + str(i5).strip() + "\n" + str(g5).strip() + "\n" +
               str(ci5).strip() + "\n" + str(cr5).strip() + "\n" + str(a5).strip() + "\n" + str(r6).strip() + "\n" +
               str(e6).strip() + "\n" + str(h6).strip() + "\n" + str(w6).strip() + "\n" + str(f6).strip() + "\n" +
               str(b6).strip() + "\n" + str(i6).strip() + "\n" + str(g6).strip() + "\n" + str(ci6).strip() + "\n" +
               str(cr6).strip() + "\n" + str(a6).strip() + "\n" + str(r7).strip() + "\n" + str(e7).strip() + "\n" +
               str(h7).strip() + "\n" + str(w7).strip() + "\n" + str(f7).strip() + "\n" + str(b7).strip() + "\n" +
               str(i7).strip() + "\n" + str(g7).strip() + "\n" + str(ci7).strip() + "\n" + str(cr7).strip() + "\n" +
               str(a7).strip() + "\n" + str(r8).strip() + "\n" + str(e8).strip() + "\n" + str(h8).strip() + "\n" +
               str(w8).strip() + "\n" + str(f8).strip() + "\n" + str(b8).strip() + "\n" + str(i8).strip() + "\n" +
               str(g8).strip() + "\n" + str(ci8).strip() + "\n" + str(cr8).strip() + "\n" + str(a8).strip() + "\n" +
               str(r9).strip() + "\n" + str(e9).strip() + "\n" + str(h9).strip() + "\n" + str(w9).strip() + "\n" +
               str(f9).strip() + "\n" + str(b9).strip() + "\n" + str(i9).strip() + "\n" + str(g9).strip() + "\n" +
               str(ci9).strip() + "\n" + str(cr9).strip() + "\n" + str(a9).strip() + "\n" + str(r10).strip() + "\n" +
               str(e10).strip() + "\n" + str(h10).strip() + "\n" + str(w10).strip() + "\n" + str(f10).strip() + "\n" +
               str(b10).strip() + "\n" + str(i10).strip() + "\n" + str(g10).strip() + "\n" + str(ci10).strip() + "\n" +
               str(cr10).strip() + "\n" + str(a10).strip() + "\n" + str(r11).strip() + "\n" + str(e11).strip() + "\n" +
               str(h11).strip() + "\n" + str(w11).strip() + "\n" + str(f11).strip() + "\n" + str(b11).strip() + "\n" +
               str(i11).strip() + "\n" + str(g11).strip() + "\n" + str(ci11).strip() + "\n" + str(cr11).strip() + "\n" +
               str(a11).strip() + "\n" + str(r12).strip() + "\n" + str(e12).strip() + "\n" + str(h12).strip() + "\n" +
               str(w12).strip() + "\n" + str(f12).strip() + "\n" + str(b12).strip() + "\n" + str(i12).strip() + "\n" +
               str(g12).strip() + "\n" + str(ci12).strip() + "\n" + str(cr12).strip() + "\n" + str(a12).strip())
    file.close()


def load_rename_config():
    with open(r"rename.txt", "r") as f:
        r1 = f.readline().strip()
        e1 = f.readline().strip()
        h1 = f.readline().strip()
        w1 = f.readline().strip()
        f1 = f.readline().strip()
        b1 = f.readline().strip()
        i1 = f.readline().strip()
        g1 = f.readline().strip()
        ci1 = f.readline().strip()
        cr1 = f.readline().strip()
        a1 = f.readline().strip()

        r2 = f.readline().strip()
        e2 = f.readline().strip()
        h2 = f.readline().strip()
        w2 = f.readline().strip()
        f2 = f.readline().strip()
        b2 = f.readline().strip()
        i2 = f.readline().strip()
        g2 = f.readline().strip()
        ci2 = f.readline().strip()
        cr2 = f.readline().strip()
        a2 = f.readline().strip()

        r3 = f.readline().strip()
        e3 = f.readline().strip()
        h3 = f.readline().strip()
        w3 = f.readline().strip()
        f3 = f.readline().strip()
        b3 = f.readline().strip()
        i3 = f.readline().strip()
        g3 = f.readline().strip()
        ci3 = f.readline().strip()
        cr3 = f.readline().strip()
        a3 = f.readline().strip()

        r4 = f.readline().strip()
        e4 = f.readline().strip()
        h4 = f.readline().strip()
        w4 = f.readline().strip()
        f4 = f.readline().strip()
        b4 = f.readline().strip()
        i4 = f.readline().strip()
        g4 = f.readline().strip()
        ci4 = f.readline().strip()
        cr4 = f.readline().strip()
        a4 = f.readline().strip()

        r5 = f.readline().strip()
        e5 = f.readline().strip()
        h5 = f.readline().strip()
        w5 = f.readline().strip()
        f5 = f.readline().strip()
        b5 = f.readline().strip()
        i5 = f.readline().strip()
        g5 = f.readline().strip()
        ci5 = f.readline().strip()
        cr5 = f.readline().strip()
        a5 = f.readline().strip()

        r6 = f.readline().strip()
        e6 = f.readline().strip()
        h6 = f.readline().strip()
        w6 = f.readline().strip()
        f6 = f.readline().strip()
        b6 = f.readline().strip()
        i6 = f.readline().strip()
        g6 = f.readline().strip()
        ci6 = f.readline().strip()
        cr6 = f.readline().strip()
        a6 = f.readline().strip()

        r7 = f.readline().strip()
        e7 = f.readline().strip()
        h7 = f.readline().strip()
        w7 = f.readline().strip()
        f7 = f.readline().strip()
        b7 = f.readline().strip()
        i7 = f.readline().strip()
        g7 = f.readline().strip()
        ci7 = f.readline().strip()
        cr7 = f.readline().strip()
        a7 = f.readline().strip()

        r8 = f.readline().strip()
        e8 = f.readline().strip()
        h8 = f.readline().strip()
        w8 = f.readline().strip()
        f8 = f.readline().strip()
        b8 = f.readline().strip()
        i8 = f.readline().strip()
        g8 = f.readline().strip()
        ci8 = f.readline().strip()
        cr8 = f.readline().strip()
        a8 = f.readline().strip()

        r9 = f.readline().strip()
        e9 = f.readline().strip()
        h9 = f.readline().strip()
        w9 = f.readline().strip()
        f9 = f.readline().strip()
        b9 = f.readline().strip()
        i9 = f.readline().strip()
        g9 = f.readline().strip()
        ci9 = f.readline().strip()
        cr9 = f.readline().strip()
        a9 = f.readline().strip()

        r10 = f.readline().strip()
        e10 = f.readline().strip()
        h10 = f.readline().strip()
        w10 = f.readline().strip()
        f10 = f.readline().strip()
        b10 = f.readline().strip()
        i10 = f.readline().strip()
        g10 = f.readline().strip()
        ci10 = f.readline().strip()
        cr10 = f.readline().strip()
        a10 = f.readline().strip()

        r11 = f.readline().strip()
        e11 = f.readline().strip()
        h11 = f.readline().strip()
        w11 = f.readline().strip()
        f11 = f.readline().strip()
        b11 = f.readline().strip()
        i11 = f.readline().strip()
        g11 = f.readline().strip()
        ci11 = f.readline().strip()
        cr11 = f.readline().strip()
        a11 = f.readline().strip()

        r12 = f.readline().strip()
        e12 = f.readline().strip()
        h12 = f.readline().strip()
        w12 = f.readline().strip()
        f12 = f.readline().strip()
        b12 = f.readline().strip()
        i12 = f.readline().strip()
        g12 = f.readline().strip()
        ci12 = f.readline().strip()
        cr12 = f.readline().strip()
        a12 = f.readline().strip()

        f.close()

    screens[3].ids.rent_rename.text = r1
    screens[3].ids.electricity_rename.text = e1
    screens[3].ids.heat_rename.text = h1
    screens[3].ids.water_rename.text = w1
    screens[3].ids.food_rename.text = f1
    screens[3].ids.building_rename.text = b1
    screens[3].ids.internet_rename.text = i1
    screens[3].ids.goofy_rename.text = g1
    screens[3].ids.cigarettes_rename.text = ci1
    screens[3].ids.credit_rename.text = cr1
    screens[3].ids.additional_rename.text = a1

    screens[4].ids.rent_rename.text = r2
    screens[4].ids.electricity_rename.text = e2
    screens[4].ids.heat_rename.text = h2
    screens[4].ids.water_rename.text = w2
    screens[4].ids.food_rename.text = f2
    screens[4].ids.building_rename.text = b2
    screens[4].ids.internet_rename.text = i2
    screens[4].ids.goofy_rename.text = g2
    screens[4].ids.cigarettes_rename.text = ci2
    screens[4].ids.credit_rename.text = cr2
    screens[4].ids.additional_rename.text = a2

    screens[5].ids.rent_rename.text = r3
    screens[5].ids.electricity_rename.text = e3
    screens[5].ids.heat_rename.text = h3
    screens[5].ids.water_rename.text = w3
    screens[5].ids.food_rename.text = f3
    screens[5].ids.building_rename.text = b3
    screens[5].ids.internet_rename.text = i3
    screens[5].ids.goofy_rename.text = g3
    screens[5].ids.cigarettes_rename.text = ci3
    screens[5].ids.credit_rename.text = cr3
    screens[5].ids.additional_rename.text = a3

    screens[6].ids.rent_rename.text = r4
    screens[6].ids.electricity_rename.text = e4
    screens[6].ids.heat_rename.text = h4
    screens[6].ids.water_rename.text = w4
    screens[6].ids.food_rename.text = f4
    screens[6].ids.building_rename.text = b4
    screens[6].ids.internet_rename.text = i4
    screens[6].ids.goofy_rename.text = g4
    screens[6].ids.cigarettes_rename.text = ci4
    screens[6].ids.credit_rename.text = cr4
    screens[6].ids.additional_rename.text = a4

    screens[7].ids.rent_rename.text = r5
    screens[7].ids.electricity_rename.text = e5
    screens[7].ids.heat_rename.text = h5
    screens[7].ids.water_rename.text = w5
    screens[7].ids.food_rename.text = f5
    screens[7].ids.building_rename.text = b5
    screens[7].ids.internet_rename.text = i5
    screens[7].ids.goofy_rename.text = g5
    screens[7].ids.cigarettes_rename.text = ci5
    screens[7].ids.credit_rename.text = cr5
    screens[7].ids.additional_rename.text = a5

    screens[8].ids.rent_rename.text = r6
    screens[8].ids.electricity_rename.text = e6
    screens[8].ids.heat_rename.text = h6
    screens[8].ids.water_rename.text = w6
    screens[8].ids.food_rename.text = f6
    screens[8].ids.building_rename.text = b6
    screens[8].ids.internet_rename.text = i6
    screens[8].ids.goofy_rename.text = g6
    screens[8].ids.cigarettes_rename.text = ci6
    screens[8].ids.credit_rename.text = cr6
    screens[8].ids.additional_rename.text = a6

    screens[9].ids.rent_rename.text = r7
    screens[9].ids.electricity_rename.text = e7
    screens[9].ids.heat_rename.text = h7
    screens[9].ids.water_rename.text = w7
    screens[9].ids.food_rename.text = f7
    screens[9].ids.building_rename.text = b7
    screens[9].ids.internet_rename.text = i7
    screens[9].ids.goofy_rename.text = g7
    screens[9].ids.cigarettes_rename.text = ci7
    screens[9].ids.credit_rename.text = cr7
    screens[9].ids.additional_rename.text = a7

    screens[10].ids.rent_rename.text = r8
    screens[10].ids.electricity_rename.text = e8
    screens[10].ids.heat_rename.text = h8
    screens[10].ids.water_rename.text = w8
    screens[10].ids.food_rename.text = f8
    screens[10].ids.building_rename.text = b8
    screens[10].ids.internet_rename.text = i8
    screens[10].ids.goofy_rename.text = g8
    screens[10].ids.cigarettes_rename.text = ci8
    screens[10].ids.credit_rename.text = cr8
    screens[10].ids.additional_rename.text = a8

    screens[11].ids.rent_rename.text = r9
    screens[11].ids.electricity_rename.text = e9
    screens[11].ids.heat_rename.text = h9
    screens[11].ids.water_rename.text = w9
    screens[11].ids.food_rename.text = f9
    screens[11].ids.building_rename.text = b9
    screens[11].ids.internet_rename.text = i9
    screens[11].ids.goofy_rename.text = g9
    screens[11].ids.cigarettes_rename.text = ci9
    screens[11].ids.credit_rename.text = cr9
    screens[11].ids.additional_rename.text = a9

    screens[12].ids.rent_rename.text = r10
    screens[12].ids.electricity_rename.text = e10
    screens[12].ids.heat_rename.text = h10
    screens[12].ids.water_rename.text = w10
    screens[12].ids.food_rename.text = f10
    screens[12].ids.building_rename.text = b10
    screens[12].ids.internet_rename.text = i10
    screens[12].ids.goofy_rename.text = g10
    screens[12].ids.cigarettes_rename.text = ci10
    screens[12].ids.credit_rename.text = cr10
    screens[12].ids.additional_rename.text = a10

    screens[13].ids.rent_rename.text = r11
    screens[13].ids.electricity_rename.text = e11
    screens[13].ids.heat_rename.text = h11
    screens[13].ids.water_rename.text = w11
    screens[13].ids.food_rename.text = f11
    screens[13].ids.building_rename.text = b11
    screens[13].ids.internet_rename.text = i11
    screens[13].ids.goofy_rename.text = g11
    screens[13].ids.cigarettes_rename.text = ci11
    screens[13].ids.credit_rename.text = cr11
    screens[13].ids.additional_rename.text = a11

    screens[14].ids.rent_rename.text = r12
    screens[14].ids.electricity_rename.text = e12
    screens[14].ids.heat_rename.text = h12
    screens[14].ids.water_rename.text = w12
    screens[14].ids.food_rename.text = f12
    screens[14].ids.building_rename.text = b12
    screens[14].ids.internet_rename.text = i12
    screens[14].ids.goofy_rename.text = g12
    screens[14].ids.cigarettes_rename.text = ci12
    screens[14].ids.credit_rename.text = cr12
    screens[14].ids.additional_rename.text = a12


# Saving CheckBox details and Reloading the same Config on Application Restart
def save_checkbox_config():
    r1 = int(screens[3].ids.rent_check.active)
    e1 = int(screens[3].ids.electricity_check.active)
    h1 = int(screens[3].ids.heat_check.active)
    w1 = int(screens[3].ids.water_check.active)
    f1 = int(screens[3].ids.food_check.active)
    b1 = int(screens[3].ids.building_check.active)
    i1 = int(screens[3].ids.internet_check.active)
    g1 = int(screens[3].ids.goofy_check.active)
    ci1 = int(screens[3].ids.cigarettes_check.active)
    cr1 = int(screens[3].ids.credit_check.active)
    a1 = int(screens[3].ids.additional_check.active)

    r2 = int(screens[4].ids.rent_check.active)
    e2 = int(screens[4].ids.electricity_check.active)
    h2 = int(screens[4].ids.heat_check.active)
    w2 = int(screens[4].ids.water_check.active)
    f2 = int(screens[4].ids.food_check.active)
    b2 = int(screens[4].ids.building_check.active)
    i2 = int(screens[4].ids.internet_check.active)
    g2 = int(screens[4].ids.goofy_check.active)
    ci2 = int(screens[4].ids.cigarettes_check.active)
    cr2 = int(screens[4].ids.credit_check.active)
    a2 = int(screens[4].ids.additional_check.active)

    r3 = int(screens[5].ids.rent_check.active)
    e3 = int(screens[5].ids.electricity_check.active)
    h3 = int(screens[5].ids.heat_check.active)
    w3 = int(screens[5].ids.water_check.active)
    f3 = int(screens[5].ids.food_check.active)
    b3 = int(screens[5].ids.building_check.active)
    i3 = int(screens[5].ids.internet_check.active)
    g3 = int(screens[5].ids.goofy_check.active)
    ci3 = int(screens[5].ids.cigarettes_check.active)
    cr3 = int(screens[5].ids.credit_check.active)
    a3 = int(screens[5].ids.additional_check.active)

    r4 = int(screens[6].ids.rent_check.active)
    e4 = int(screens[6].ids.electricity_check.active)
    h4 = int(screens[6].ids.heat_check.active)
    w4 = int(screens[6].ids.water_check.active)
    f4 = int(screens[6].ids.food_check.active)
    b4 = int(screens[6].ids.building_check.active)
    i4 = int(screens[6].ids.internet_check.active)
    g4 = int(screens[6].ids.goofy_check.active)
    ci4 = int(screens[6].ids.cigarettes_check.active)
    cr4 = int(screens[6].ids.credit_check.active)
    a4 = int(screens[6].ids.additional_check.active)

    r5 = int(screens[7].ids.rent_check.active)
    e5 = int(screens[7].ids.electricity_check.active)
    h5 = int(screens[7].ids.heat_check.active)
    w5 = int(screens[7].ids.water_check.active)
    f5 = int(screens[7].ids.food_check.active)
    b5 = int(screens[7].ids.building_check.active)
    i5 = int(screens[7].ids.internet_check.active)
    g5 = int(screens[7].ids.goofy_check.active)
    ci5 = int(screens[7].ids.cigarettes_check.active)
    cr5 = int(screens[7].ids.credit_check.active)
    a5 = int(screens[7].ids.additional_check.active)

    r6 = int(screens[8].ids.rent_check.active)
    e6 = int(screens[8].ids.electricity_check.active)
    h6 = int(screens[8].ids.heat_check.active)
    w6 = int(screens[8].ids.water_check.active)
    f6 = int(screens[8].ids.food_check.active)
    b6 = int(screens[8].ids.building_check.active)
    i6 = int(screens[8].ids.internet_check.active)
    g6 = int(screens[8].ids.goofy_check.active)
    ci6 = int(screens[8].ids.cigarettes_check.active)
    cr6 = int(screens[8].ids.credit_check.active)
    a6 = int(screens[8].ids.additional_check.active)

    r7 = int(screens[9].ids.rent_check.active)
    e7 = int(screens[9].ids.electricity_check.active)
    h7 = int(screens[9].ids.heat_check.active)
    w7 = int(screens[9].ids.water_check.active)
    f7 = int(screens[9].ids.food_check.active)
    b7 = int(screens[9].ids.building_check.active)
    i7 = int(screens[9].ids.internet_check.active)
    g7 = int(screens[9].ids.goofy_check.active)
    ci7 = int(screens[9].ids.cigarettes_check.active)
    cr7 = int(screens[9].ids.credit_check.active)
    a7 = int(screens[9].ids.additional_check.active)

    r8 = int(screens[10].ids.rent_check.active)
    e8 = int(screens[10].ids.electricity_check.active)
    h8 = int(screens[10].ids.heat_check.active)
    w8 = int(screens[10].ids.water_check.active)
    f8 = int(screens[10].ids.food_check.active)
    b8 = int(screens[10].ids.building_check.active)
    i8 = int(screens[10].ids.internet_check.active)
    g8 = int(screens[10].ids.goofy_check.active)
    ci8 = int(screens[10].ids.cigarettes_check.active)
    cr8 = int(screens[10].ids.credit_check.active)
    a8 = int(screens[10].ids.additional_check.active)

    r9 = int(screens[11].ids.rent_check.active)
    e9 = int(screens[11].ids.electricity_check.active)
    h9 = int(screens[11].ids.heat_check.active)
    w9 = int(screens[11].ids.water_check.active)
    f9 = int(screens[11].ids.food_check.active)
    b9 = int(screens[11].ids.building_check.active)
    i9 = int(screens[11].ids.internet_check.active)
    g9 = int(screens[11].ids.goofy_check.active)
    ci9 = int(screens[11].ids.cigarettes_check.active)
    cr9 = int(screens[11].ids.credit_check.active)
    a9 = int(screens[11].ids.additional_check.active)

    r10 = int(screens[12].ids.rent_check.active)
    e10 = int(screens[12].ids.electricity_check.active)
    h10 = int(screens[12].ids.heat_check.active)
    w10 = int(screens[12].ids.water_check.active)
    f10 = int(screens[12].ids.food_check.active)
    b10 = int(screens[12].ids.building_check.active)
    i10 = int(screens[12].ids.internet_check.active)
    g10 = int(screens[12].ids.goofy_check.active)
    ci10 = int(screens[12].ids.cigarettes_check.active)
    cr10 = int(screens[12].ids.credit_check.active)
    a10 = int(screens[12].ids.additional_check.active)

    r11 = int(screens[13].ids.rent_check.active)
    e11 = int(screens[13].ids.electricity_check.active)
    h11 = int(screens[13].ids.heat_check.active)
    w11 = int(screens[13].ids.water_check.active)
    f11 = int(screens[13].ids.food_check.active)
    b11 = int(screens[13].ids.building_check.active)
    i11 = int(screens[13].ids.internet_check.active)
    g11 = int(screens[13].ids.goofy_check.active)
    ci11 = int(screens[13].ids.cigarettes_check.active)
    cr11 = int(screens[13].ids.credit_check.active)
    a11 = int(screens[13].ids.additional_check.active)

    r12 = int(screens[14].ids.rent_check.active)
    e12 = int(screens[14].ids.electricity_check.active)
    h12 = int(screens[14].ids.heat_check.active)
    w12 = int(screens[14].ids.water_check.active)
    f12 = int(screens[14].ids.food_check.active)
    b12 = int(screens[14].ids.building_check.active)
    i12 = int(screens[14].ids.internet_check.active)
    g12 = int(screens[14].ids.goofy_check.active)
    ci12 = int(screens[14].ids.cigarettes_check.active)
    cr12 = int(screens[14].ids.credit_check.active)
    a12 = int(screens[14].ids.additional_check.active)

    file = open(r"checkbox.txt", "w+")
    file.write(str(r1).strip() + "\n" + str(e1).strip() + "\n" + str(h1).strip() + "\n" + str(w1).strip() + "\n" +
               str(f1).strip() + "\n" + str(b1).strip() + "\n" + str(i1).strip() + "\n" + str(g1).strip() + "\n" +
               str(ci1).strip() + "\n" + str(cr1).strip() + "\n" + str(a1).strip() + "\n" + str(r2).strip() + "\n" +
               str(e2).strip() + "\n" + str(h2).strip() + "\n" + str(w2).strip() + "\n" + str(f2).strip() + "\n" +
               str(b2).strip() + "\n" + str(i2).strip() + "\n" + str(g2).strip() + "\n" + str(ci2).strip() + "\n" +
               str(cr2).strip() + "\n" + str(a2).strip() + "\n" + str(r3).strip() + "\n" + str(e3).strip() + "\n" +
               str(h3).strip() + "\n" + str(w3).strip() + "\n" + str(f3).strip() + "\n" + str(b3).strip() + "\n" +
               str(i3).strip() + "\n" + str(g3).strip() + "\n" + str(ci3).strip() + "\n" + str(cr3).strip() + "\n" +
               str(a3).strip() + "\n" + str(r4).strip() + "\n" + str(e4).strip() + "\n" + str(h4).strip() + "\n" +
               str(w4).strip() + "\n" + str(f4).strip() + "\n" + str(b4).strip() + "\n" + str(i4).strip() + "\n" +
               str(g4).strip() + "\n" + str(ci4).strip() + "\n" + str(cr4).strip() + "\n" + str(a4).strip() + "\n" +
               str(r5).strip() + "\n" + str(e5).strip() + "\n" + str(h5).strip() + "\n" + str(w5).strip() + "\n" +
               str(f5).strip() + "\n" + str(b5).strip() + "\n" + str(i5).strip() + "\n" + str(g5).strip() + "\n" +
               str(ci5).strip() + "\n" + str(cr5).strip() + "\n" + str(a5).strip() + "\n" + str(r6).strip() + "\n" +
               str(e6).strip() + "\n" + str(h6).strip() + "\n" + str(w6).strip() + "\n" + str(f6).strip() + "\n" +
               str(b6).strip() + "\n" + str(i6).strip() + "\n" + str(g6).strip() + "\n" + str(ci6).strip() + "\n" +
               str(cr6).strip() + "\n" + str(a6).strip() + "\n" + str(r7).strip() + "\n" + str(e7).strip() + "\n" +
               str(h7).strip() + "\n" + str(w7).strip() + "\n" + str(f7).strip() + "\n" + str(b7).strip() + "\n" +
               str(i7).strip() + "\n" + str(g7).strip() + "\n" + str(ci7).strip() + "\n" + str(cr7).strip() + "\n" +
               str(a7).strip() + "\n" + str(r8).strip() + "\n" + str(e8).strip() + "\n" + str(h8).strip() + "\n" +
               str(w8).strip() + "\n" + str(f8).strip() + "\n" + str(b8).strip() + "\n" + str(i8).strip() + "\n" +
               str(g8).strip() + "\n" + str(ci8).strip() + "\n" + str(cr8).strip() + "\n" + str(a8).strip() + "\n" +
               str(r9).strip() + "\n" + str(e9).strip() + "\n" + str(h9).strip() + "\n" + str(w9).strip() + "\n" +
               str(f9).strip() + "\n" + str(b9).strip() + "\n" + str(i9).strip() + "\n" + str(g9).strip() + "\n" +
               str(ci9).strip() + "\n" + str(cr9).strip() + "\n" + str(a9).strip() + "\n" + str(r10).strip() + "\n" +
               str(e10).strip() + "\n" + str(h10).strip() + "\n" + str(w10).strip() + "\n" + str(f10).strip() + "\n" +
               str(b10).strip() + "\n" + str(i10).strip() + "\n" + str(g10).strip() + "\n" + str(ci10).strip() + "\n" +
               str(cr10).strip() + "\n" + str(a10).strip() + "\n" + str(r11).strip() + "\n" + str(e11).strip() + "\n" +
               str(h11).strip() + "\n" + str(w11).strip() + "\n" + str(f11).strip() + "\n" + str(b11).strip() + "\n" +
               str(i11).strip() + "\n" + str(g11).strip() + "\n" + str(ci11).strip() + "\n" + str(cr11).strip() + "\n" +
               str(a11).strip() + "\n" + str(r12).strip() + "\n" + str(e12).strip() + "\n" + str(h12).strip() + "\n" +
               str(w12).strip() + "\n" + str(f12).strip() + "\n" + str(b12).strip() + "\n" + str(i12).strip() + "\n" +
               str(g12).strip() + "\n" + str(ci12).strip() + "\n" + str(cr12).strip() + "\n" + str(a12).strip())
    file.close()

    if r1 or e1 or h1 or w1 or f1 or b1 or i1 or g1 or ci1 or cr1 or a1 == 0:
        screens[3].hide()
        screens[3].show()
        screens[3].show_total_paid()
    else:
        screens[3].hide()
        screens[3].show()
        screens[3].show_total_paid()
    if r2 or e2 or h2 or w2 or f2 or b2 or i2 or g2 or ci2 or cr2 or a2 == 0:
        screens[4].hide()
        screens[4].show()
        screens[4].show_total_paid()
    else:
        screens[4].hide()
        screens[4].show()
        screens[4].show_total_paid()
    if r3 or e3 or h3 or w3 or f3 or b3 or i3 or g3 or ci3 or cr3 or a3 == 0:
        screens[5].hide()
        screens[5].show()
        screens[5].show_total_paid()
    else:
        screens[5].hide()
        screens[5].show()
        screens[5].show_total_paid()
    if r4 or e4 or h4 or w4 or f4 or b4 or i4 or g4 or ci4 or cr4 or a4 == 0:
        screens[6].hide()
        screens[6].show()
        screens[6].show_total_paid()
    else:
        screens[6].hide()
        screens[6].show()
        screens[6].show_total_paid()
    if r5 or e5 or h5 or w5 or f5 or b5 or i5 or g5 or ci5 or cr5 or a5 == 0:
        screens[7].hide()
        screens[7].show()
        screens[7].show_total_paid()
    else:
        screens[7].hide()
        screens[7].show()
        screens[7].show_total_paid()
    if r6 or e6 or h6 or w6 or f6 or b6 or i6 or g6 or ci6 or cr6 or a6 == 0:
        screens[8].hide()
        screens[8].show()
        screens[8].show_total_paid()
    else:
        screens[8].hide()
        screens[8].show()
        screens[8].show_total_paid()
    if r7 or e7 or h7 or w7 or f7 or b7 or i7 or g7 or ci7 or cr7 or a7 == 0:
        screens[9].hide()
        screens[9].show()
        screens[9].show_total_paid()
    else:
        screens[9].hide()
        screens[9].show()
        screens[9].show_total_paid()
    if r8 or e8 or h8 or w8 or f8 or b8 or i8 or g8 or ci8 or cr8 or a8 == 0:
        screens[10].hide()
        screens[10].show()
        screens[10].show_total_paid()
    else:
        screens[10].hide()
        screens[10].show()
        screens[10].show_total_paid()
    if r9 or e9 or h9 or w9 or f9 or b9 or i9 or g9 or ci9 or cr9 or a9 == 0:
        screens[11].hide()
        screens[11].show()
        screens[11].show_total_paid()
    else:
        screens[11].hide()
        screens[11].show()
        screens[11].show_total_paid()
    if r10 or e10 or h10 or w10 or f10 or b10 or i10 or g10 or ci10 or cr10 or a10 == 0:
        screens[12].hide()
        screens[12].show()
        screens[12].show_total_paid()
    else:
        screens[12].hide()
        screens[12].show()
        screens[12].show_total_paid()
    if r11 or e11 or h11 or w11 or f11 or b11 or i11 or g11 or ci11 or cr11 or a11 == 0:
        screens[13].hide()
        screens[13].show()
        screens[13].show_total_paid()
    else:
        screens[13].hide()
        screens[13].show()
        screens[13].show_total_paid()
    if r12 or e12 or h12 or w12 or f12 or b12 or i12 or g12 or ci12 or cr12 or a12 == 0:
        screens[14].hide()
        screens[14].show()
        screens[14].show_total_paid()
    else:
        screens[14].hide()
        screens[14].show()
        screens[14].show_total_paid()


def load_checkbox_config():
    with open(r"checkbox.txt", "r") as f:
        r1 = f.readline().strip()
        e1 = f.readline().strip()
        h1 = f.readline().strip()
        w1 = f.readline().strip()
        f1 = f.readline().strip()
        b1 = f.readline().strip()
        i1 = f.readline().strip()
        g1 = f.readline().strip()
        ci1 = f.readline().strip()
        cr1 = f.readline().strip()
        a1 = f.readline().strip()

        r2 = f.readline().strip()
        e2 = f.readline().strip()
        h2 = f.readline().strip()
        w2 = f.readline().strip()
        f2 = f.readline().strip()
        b2 = f.readline().strip()
        i2 = f.readline().strip()
        g2 = f.readline().strip()
        ci2 = f.readline().strip()
        cr2 = f.readline().strip()
        a2 = f.readline().strip()

        r3 = f.readline().strip()
        e3 = f.readline().strip()
        h3 = f.readline().strip()
        w3 = f.readline().strip()
        f3 = f.readline().strip()
        b3 = f.readline().strip()
        i3 = f.readline().strip()
        g3 = f.readline().strip()
        ci3 = f.readline().strip()
        cr3 = f.readline().strip()
        a3 = f.readline().strip()

        r4 = f.readline().strip()
        e4 = f.readline().strip()
        h4 = f.readline().strip()
        w4 = f.readline().strip()
        f4 = f.readline().strip()
        b4 = f.readline().strip()
        i4 = f.readline().strip()
        g4 = f.readline().strip()
        ci4 = f.readline().strip()
        cr4 = f.readline().strip()
        a4 = f.readline().strip()

        r5 = f.readline().strip()
        e5 = f.readline().strip()
        h5 = f.readline().strip()
        w5 = f.readline().strip()
        f5 = f.readline().strip()
        b5 = f.readline().strip()
        i5 = f.readline().strip()
        g5 = f.readline().strip()
        ci5 = f.readline().strip()
        cr5 = f.readline().strip()
        a5 = f.readline().strip()

        r6 = f.readline().strip()
        e6 = f.readline().strip()
        h6 = f.readline().strip()
        w6 = f.readline().strip()
        f6 = f.readline().strip()
        b6 = f.readline().strip()
        i6 = f.readline().strip()
        g6 = f.readline().strip()
        ci6 = f.readline().strip()
        cr6 = f.readline().strip()
        a6 = f.readline().strip()

        r7 = f.readline().strip()
        e7 = f.readline().strip()
        h7 = f.readline().strip()
        w7 = f.readline().strip()
        f7 = f.readline().strip()
        b7 = f.readline().strip()
        i7 = f.readline().strip()
        g7 = f.readline().strip()
        ci7 = f.readline().strip()
        cr7 = f.readline().strip()
        a7 = f.readline().strip()

        r8 = f.readline().strip()
        e8 = f.readline().strip()
        h8 = f.readline().strip()
        w8 = f.readline().strip()
        f8 = f.readline().strip()
        b8 = f.readline().strip()
        i8 = f.readline().strip()
        g8 = f.readline().strip()
        ci8 = f.readline().strip()
        cr8 = f.readline().strip()
        a8 = f.readline().strip()

        r9 = f.readline().strip()
        e9 = f.readline().strip()
        h9 = f.readline().strip()
        w9 = f.readline().strip()
        f9 = f.readline().strip()
        b9 = f.readline().strip()
        i9 = f.readline().strip()
        g9 = f.readline().strip()
        ci9 = f.readline().strip()
        cr9 = f.readline().strip()
        a9 = f.readline().strip()

        r10 = f.readline().strip()
        e10 = f.readline().strip()
        h10 = f.readline().strip()
        w10 = f.readline().strip()
        f10 = f.readline().strip()
        b10 = f.readline().strip()
        i10 = f.readline().strip()
        g10 = f.readline().strip()
        ci10 = f.readline().strip()
        cr10 = f.readline().strip()
        a10 = f.readline().strip()

        r11 = f.readline().strip()
        e11 = f.readline().strip()
        h11 = f.readline().strip()
        w11 = f.readline().strip()
        f11 = f.readline().strip()
        b11 = f.readline().strip()
        i11 = f.readline().strip()
        g11 = f.readline().strip()
        ci11 = f.readline().strip()
        cr11 = f.readline().strip()
        a11 = f.readline().strip()

        r12 = f.readline().strip()
        e12 = f.readline().strip()
        h12 = f.readline().strip()
        w12 = f.readline().strip()
        f12 = f.readline().strip()
        b12 = f.readline().strip()
        i12 = f.readline().strip()
        g12 = f.readline().strip()
        ci12 = f.readline().strip()
        cr12 = f.readline().strip()
        a12 = f.readline().strip()

        if r1 == '1':
            screens[3].ids.rent_check.active = True
        if e1 == '1':
            screens[3].ids.electricity_check.active = True
        if h1 == '1':
            screens[3].ids.heat_check.active = True
        if w1 == '1':
            screens[3].ids.water_check.active = True
        if f1 == '1':
            screens[3].ids.food_check.active = True
        if b1 == '1':
            screens[3].ids.building_check.active = True
        if i1 == '1':
            screens[3].ids.internet_check.active = True
        if g1 == '1':
            screens[3].ids.goofy_check.active = True
        if ci1 == '1':
            screens[3].ids.cigarettes_check.active = True
        if cr1 == '1':
            screens[3].ids.credit_check.active = True
        if a1 == '1':
            screens[3].ids.additional_check.active = True

        if r2 == '1':
            screens[4].ids.rent_check.active = True
        if e2 == '1':
            screens[4].ids.electricity_check.active = True
        if h2 == '1':
            screens[4].ids.heat_check.active = True
        if w2 == '1':
            screens[4].ids.water_check.active = True
        if f2 == '1':
            screens[4].ids.food_check.active = True
        if b2 == '1':
            screens[4].ids.building_check.active = True
        if i2 == '1':
            screens[4].ids.internet_check.active = True
        if g2 == '1':
            screens[4].ids.goofy_check.active = True
        if ci2 == '1':
            screens[4].ids.cigarettes_check.active = True
        if cr2 == '1':
            screens[4].ids.credit_check.active = True
        if a2 == '1':
            screens[4].ids.additional_check.active = True

        if r3 == '1':
            screens[5].ids.rent_check.active = True
        if e3 == '1':
            screens[5].ids.electricity_check.active = True
        if h3 == '1':
            screens[5].ids.heat_check.active = True
        if w3 == '1':
            screens[5].ids.water_check.active = True
        if f3 == '1':
            screens[5].ids.food_check.active = True
        if b3 == '1':
            screens[5].ids.building_check.active = True
        if i3 == '1':
            screens[5].ids.internet_check.active = True
        if g3 == '1':
            screens[5].ids.goofy_check.active = True
        if ci3 == '1':
            screens[5].ids.cigarettes_check.active = True
        if cr3 == '1':
            screens[5].ids.credit_check.active = True
        if a3 == '1':
            screens[5].ids.additional_check.active = True

        if r4 == '1':
            screens[6].ids.rent_check.active = True
        if e4 == '1':
            screens[6].ids.electricity_check.active = True
        if h4 == '1':
            screens[6].ids.heat_check.active = True
        if w4 == '1':
            screens[6].ids.water_check.active = True
        if f4 == '1':
            screens[6].ids.food_check.active = True
        if b4 == '1':
            screens[6].ids.building_check.active = True
        if i4 == '1':
            screens[6].ids.internet_check.active = True
        if g4 == '1':
            screens[6].ids.goofy_check.active = True
        if ci4 == '1':
            screens[6].ids.cigarettes_check.active = True
        if cr4 == '1':
            screens[6].ids.credit_check.active = True
        if a4 == '1':
            screens[6].ids.additional_check.active = True

        if r5 == '1':
            screens[7].ids.rent_check.active = True
        if e5 == '1':
            screens[7].ids.electricity_check.active = True
        if h5 == '1':
            screens[7].ids.heat_check.active = True
        if w5 == '1':
            screens[7].ids.water_check.active = True
        if f5 == '1':
            screens[7].ids.food_check.active = True
        if b5 == '1':
            screens[7].ids.building_check.active = True
        if i5 == '1':
            screens[7].ids.internet_check.active = True
        if g5 == '1':
            screens[7].ids.goofy_check.active = True
        if ci5 == '1':
            screens[7].ids.cigarettes_check.active = True
        if cr5 == '1':
            screens[7].ids.credit_check.active = True
        if a5 == '1':
            screens[7].ids.additional_check.active = True

        if r6 == '1':
            screens[8].ids.rent_check.active = True
        if e6 == '1':
            screens[8].ids.electricity_check.active = True
        if h6 == '1':
            screens[8].ids.heat_check.active = True
        if w6 == '1':
            screens[8].ids.water_check.active = True
        if f6 == '1':
            screens[8].ids.food_check.active = True
        if b6 == '1':
            screens[8].ids.building_check.active = True
        if i6 == '1':
            screens[8].ids.internet_check.active = True
        if g6 == '1':
            screens[8].ids.goofy_check.active = True
        if ci6 == '1':
            screens[8].ids.cigarettes_check.active = True
        if cr6 == '1':
            screens[8].ids.credit_check.active = True
        if a6 == '1':
            screens[8].ids.additional_check.active = True

        if r7 == '1':
            screens[9].ids.rent_check.active = True
        if e7 == '1':
            screens[9].ids.electricity_check.active = True
        if h7 == '1':
            screens[9].ids.heat_check.active = True
        if w7 == '1':
            screens[9].ids.water_check.active = True
        if f7 == '1':
            screens[9].ids.food_check.active = True
        if b7 == '1':
            screens[9].ids.building_check.active = True
        if i7 == '1':
            screens[9].ids.internet_check.active = True
        if g7 == '1':
            screens[9].ids.goofy_check.active = True
        if ci7 == '1':
            screens[9].ids.cigarettes_check.active = True
        if cr7 == '1':
            screens[9].ids.credit_check.active = True
        if a7 == '1':
            screens[9].ids.additional_check.active = True

        if r8 == '1':
            screens[10].ids.rent_check.active = True
        if e8 == '1':
            screens[10].ids.electricity_check.active = True
        if h8 == '1':
            screens[10].ids.heat_check.active = True
        if w8 == '1':
            screens[10].ids.water_check.active = True
        if f8 == '1':
            screens[10].ids.food_check.active = True
        if b8 == '1':
            screens[10].ids.building_check.active = True
        if i8 == '1':
            screens[10].ids.internet_check.active = True
        if g8 == '1':
            screens[10].ids.goofy_check.active = True
        if ci8 == '1':
            screens[10].ids.cigarettes_check.active = True
        if cr8 == '1':
            screens[10].ids.credit_check.active = True
        if a8 == '1':
            screens[10].ids.additional_check.active = True

        if r9 == '1':
            screens[11].ids.rent_check.active = True
        if e9 == '1':
            screens[11].ids.electricity_check.active = True
        if h9 == '1':
            screens[11].ids.heat_check.active = True
        if w9 == '1':
            screens[11].ids.water_check.active = True
        if f9 == '1':
            screens[11].ids.food_check.active = True
        if b9 == '1':
            screens[11].ids.building_check.active = True
        if i9 == '1':
            screens[11].ids.internet_check.active = True
        if g9 == '1':
            screens[11].ids.goofy_check.active = True
        if ci9 == '1':
            screens[11].ids.cigarettes_check.active = True
        if cr9 == '1':
            screens[11].ids.credit_check.active = True
        if a9 == '1':
            screens[11].ids.additional_check.active = True

        if r10 == '1':
            screens[12].ids.rent_check.active = True
        if e10 == '1':
            screens[12].ids.electricity_check.active = True
        if h10 == '1':
            screens[12].ids.heat_check.active = True
        if w10 == '1':
            screens[12].ids.water_check.active = True
        if f10 == '1':
            screens[12].ids.food_check.active = True
        if b10 == '1':
            screens[12].ids.building_check.active = True
        if i10 == '1':
            screens[12].ids.internet_check.active = True
        if g10 == '1':
            screens[12].ids.goofy_check.active = True
        if ci10 == '1':
            screens[12].ids.cigarettes_check.active = True
        if cr10 == '1':
            screens[12].ids.credit_check.active = True
        if a10 == '1':
            screens[12].ids.additional_check.active = True

        if r11 == '1':
            screens[13].ids.rent_check.active = True
        if e11 == '1':
            screens[13].ids.electricity_check.active = True
        if h11 == '1':
            screens[13].ids.heat_check.active = True
        if w11 == '1':
            screens[13].ids.water_check.active = True
        if f11 == '1':
            screens[13].ids.food_check.active = True
        if b11 == '1':
            screens[13].ids.building_check.active = True
        if i11 == '1':
            screens[13].ids.internet_check.active = True
        if g11 == '1':
            screens[13].ids.goofy_check.active = True
        if ci11 == '1':
            screens[13].ids.cigarettes_check.active = True
        if cr11 == '1':
            screens[13].ids.credit_check.active = True
        if a11 == '1':
            screens[13].ids.additional_check.active = True

        if r12 == '1':
            screens[14].ids.rent_check.active = True
        if e12 == '1':
            screens[14].ids.electricity_check.active = True
        if h12 == '1':
            screens[14].ids.heat_check.active = True
        if w12 == '1':
            screens[14].ids.water_check.active = True
        if f12 == '1':
            screens[14].ids.food_check.active = True
        if b12 == '1':
            screens[14].ids.building_check.active = True
        if i12 == '1':
            screens[14].ids.internet_check.active = True
        if g12 == '1':
            screens[14].ids.goofy_check.active = True
        if ci12 == '1':
            screens[14].ids.cigarettes_check.active = True
        if cr12 == '1':
            screens[14].ids.credit_check.active = True
        if a12 == '1':
            screens[14].ids.additional_check.active = True

        f.close()


# General Configuration
def main_config():
    load_rename_config()
    load_checkbox_config()

    screens[3].hide()
    screens[3].ids.show.text = 'Show Table'
    screens[4].hide()
    screens[4].ids.show.text = 'Show Table'
    screens[5].hide()
    screens[5].ids.show.text = 'Show Table'
    screens[6].hide()
    screens[6].ids.show.text = 'Show Table'
    screens[7].hide()
    screens[7].ids.show.text = 'Show Table'
    screens[8].hide()
    screens[8].ids.show.text = 'Show Table'
    screens[9].hide()
    screens[9].ids.show.text = 'Show Table'
    screens[10].hide()
    screens[10].ids.show.text = 'Show Table'
    screens[11].hide()
    screens[11].ids.show.text = 'Show Table'
    screens[12].hide()
    screens[12].ids.show.text = 'Show Table'
    screens[13].hide()
    screens[13].ids.show.text = 'Show Table'
    screens[14].hide()
    screens[14].ids.show.text = 'Show Table'


# Building the Login, Create Account and Main Screens
class Login(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def login_btn(self):
        if db.validate(self.username.text, self.password.text):
            self.reset()
            sm.current = 'main'
        else:
            pop = Popup(title='Invalid Login', content=Label(text="Invalid username or password."),
                        size_hint=(None, None), size=(400, 400))
            pop.open()

    def reset(self):
        self.username.text = ""
        self.password.text = ""


class CreateAccount(Screen):
    create_username = ObjectProperty(None)
    create_email = ObjectProperty(None)
    create_password = ObjectProperty(None)

    def submit_login(self):
        if self.create_username.text != "":
            if self.create_email.text != "" and self.create_email.text.count("@") == 1 and \
                    self.create_email.text.count(".") > 0:
                if self.create_password.text != "":
                    db.add_user(self.create_username.text, self.create_email.text, self.create_password.text)
                    self.reset()
                    sm.current = 'login'
                else:
                    pop = Popup(title='Invalid Form',
                                content=Label(text="Please enter a valid password."),
                                size_hint=(None, None), size=(400, 400))
                    pop.open()
            else:
                pop = Popup(title='Invalid Form', content=Label(text="Please enter a valid email."),
                            size_hint=(None, None), size=(400, 400))
                pop.open()
        else:
            pop = Popup(title='Invalid Form', content=Label(text="Please enter a valid username."),
                        size_hint=(None, None), size=(400, 400))
            pop.open()

    def login(self):
        self.reset()
        sm.current = 'main'

    def reset(self):
        self.create_username.text = ""
        self.create_email.text = ""
        self.create_password.text = ""


class Main(Screen):
    global jan_res, feb_res, mar_res, apr_res, may_res, jun_res, jul_res, aug_res, sep_res, oct_res, nov_res, dec_res

    @staticmethod
    def show():
        screens[15].show()
        screens[15].rule()
        screens[15].ids.save_report.disabled = True

    @staticmethod
    def save_disable():
        screens[3].ids.save.disabled = True
        screens[3].ids.save_rename.disabled = True
        screens[4].ids.save.disabled = True
        screens[4].ids.save_rename.disabled = True
        screens[5].ids.save.disabled = True
        screens[5].ids.save_rename.disabled = True
        screens[6].ids.save.disabled = True
        screens[6].ids.save_rename.disabled = True
        screens[7].ids.save.disabled = True
        screens[7].ids.save_rename.disabled = True
        screens[8].ids.save.disabled = True
        screens[8].ids.save_rename.disabled = True
        screens[9].ids.save.disabled = True
        screens[9].ids.save_rename.disabled = True
        screens[10].ids.save.disabled = True
        screens[10].ids.save_rename.disabled = True
        screens[11].ids.save.disabled = True
        screens[11].ids.save_rename.disabled = True
        screens[12].ids.save.disabled = True
        screens[12].ids.save_rename.disabled = True
        screens[13].ids.save.disabled = True
        screens[13].ids.save_rename.disabled = True
        screens[14].ids.save.disabled = True
        screens[14].ids.save_rename.disabled = True

    @staticmethod
    def export_data():
        screens[3].show_total_paid()
        screens[4].show_total_paid()
        screens[5].show_total_paid()
        screens[6].show_total_paid()
        screens[7].show_total_paid()
        screens[8].show_total_paid()
        screens[9].show_total_paid()
        screens[10].show_total_paid()
        screens[11].show_total_paid()
        screens[12].show_total_paid()
        screens[13].show_total_paid()
        screens[14].show_total_paid()

        january = screens[3].ids.show_total_paid_4.text
        february = screens[4].ids.show_total_paid_4.text
        march = screens[5].ids.show_total_paid_4.text
        april = screens[6].ids.show_total_paid_4.text
        may = screens[7].ids.show_total_paid_4.text
        june = screens[8].ids.show_total_paid_4.text
        july = screens[9].ids.show_total_paid_4.text
        august = screens[10].ids.show_total_paid_4.text
        september = screens[11].ids.show_total_paid_4.text
        october = screens[12].ids.show_total_paid_4.text
        november = screens[13].ids.show_total_paid_4.text
        december = screens[14].ids.show_total_paid_4.text

        if january == "":
            january = 0
        if february == "":
            february = 0
        if march == "":
            march = 0
        if april == "":
            april = 0
        if may == "":
            may = 0
        if june == "":
            june = 0
        if july == "":
            july = 0
        if august == "":
            august = 0
        if september == "":
            september = 0
        if october == "":
            october = 0
        if november == "":
            november = 0
        if december == "":
            december = 0

        screens[15].ids.bill_1.text = str(january)
        screens[15].ids.bill_2.text = str(february)
        screens[15].ids.bill_3.text = str(march)
        screens[15].ids.bill_4.text = str(april)
        screens[15].ids.bill_5.text = str(may)
        screens[15].ids.bill_6.text = str(june)
        screens[15].ids.bill_7.text = str(july)
        screens[15].ids.bill_8.text = str(august)
        screens[15].ids.bill_9.text = str(september)
        screens[15].ids.bill_10.text = str(october)
        screens[15].ids.bill_11.text = str(november)
        screens[15].ids.bill_12.text = str(december)

        screens[15].show()

    @staticmethod
    def calculate_left():
        global jan_res, feb_res, mar_res, apr_res, may_res, jun_res, jul_res, \
            aug_res, sep_res, oct_res, nov_res, dec_res

        screens[3].show_total_paid()
        screens[4].show_total_paid()
        screens[5].show_total_paid()
        screens[6].show_total_paid()
        screens[7].show_total_paid()
        screens[8].show_total_paid()
        screens[9].show_total_paid()
        screens[10].show_total_paid()
        screens[11].show_total_paid()
        screens[12].show_total_paid()
        screens[13].show_total_paid()
        screens[14].show_total_paid()

        january = screens[3].ids.show_total_paid_4.text
        february = screens[4].ids.show_total_paid_4.text
        march = screens[5].ids.show_total_paid_4.text
        april = screens[6].ids.show_total_paid_4.text
        may = screens[7].ids.show_total_paid_4.text
        june = screens[8].ids.show_total_paid_4.text
        july = screens[9].ids.show_total_paid_4.text
        august = screens[10].ids.show_total_paid_4.text
        september = screens[11].ids.show_total_paid_4.text
        october = screens[12].ids.show_total_paid_4.text
        november = screens[13].ids.show_total_paid_4.text
        december = screens[14].ids.show_total_paid_4.text

        if january == "":
            jan_num = 0
        else:
            jan_num = int(january)
        if february == "":
            feb_num = 0
        else:
            feb_num = int(february)
        if march == "":
            mar_num = 0
        else:
            mar_num = int(march)
        if april == "":
            apr_num = 0
        else:
            apr_num = int(april)
        if may == "":
            may_num = 0
        else:
            may_num = int(may)
        if june == "":
            jun_num = 0
        else:
            jun_num = int(june)
        if july == "":
            jul_num = 0
        else:
            jul_num = int(july)
        if august == "":
            aug_num = 0
        else:
            aug_num = int(august)
        if september == "":
            sep_num = 0
        else:
            sep_num = int(september)
        if october == "":
            oct_num = 0
        else:
            oct_num = int(october)
        if november == "":
            nov_num = 0
        else:
            nov_num = int(november)
        if december == "":
            dec_num = 0
        else:
            dec_num = int(december)

        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT * FROM income WHERE oid = 1")
        records = c.fetchall()
        for record in records:
            january_income = int(record[0])
            february_income = int(record[1])
            march_income = int(record[2])
            april_income = int(record[3])
            may_income = int(record[4])
            june_income = int(record[5])
            july_income = int(record[6])
            august_income = int(record[7])
            september_income = int(record[8])
            october_income = int(record[9])
            november_income = int(record[10])
            december_income = int(record[11])

            jan_res = january_income - jan_num
            feb_res = february_income - feb_num
            mar_res = march_income - mar_num
            apr_res = april_income - apr_num
            may_res = may_income - may_num
            jun_res = june_income - jun_num
            jul_res = july_income - jul_num
            aug_res = august_income - aug_num
            sep_res = september_income - sep_num
            oct_res = october_income - oct_num
            nov_res = november_income - nov_num
            dec_res = december_income - dec_num

            screens[15].ids.after_1.text = str(jan_res)
            screens[15].ids.after_2.text = str(feb_res)
            screens[15].ids.after_3.text = str(mar_res)
            screens[15].ids.after_4.text = str(apr_res)
            screens[15].ids.after_5.text = str(may_res)
            screens[15].ids.after_6.text = str(jun_res)
            screens[15].ids.after_7.text = str(jul_res)
            screens[15].ids.after_8.text = str(aug_res)
            screens[15].ids.after_9.text = str(sep_res)
            screens[15].ids.after_10.text = str(oct_res)
            screens[15].ids.after_11.text = str(nov_res)
            screens[15].ids.after_12.text = str(dec_res)

        conn.commit()
        conn.close()

        screens[15].show()

    @staticmethod
    def calculate_others():
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT * FROM available WHERE oid = 1")
        records = c.fetchall()

        for record in records:
            january_available = int(record[0])
            february_available = int(record[1])
            march_available = int(record[2])
            april_available = int(record[3])
            may_available = int(record[4])
            june_available = int(record[5])
            july_available = int(record[6])
            august_available = int(record[7])
            september_available = int(record[8])
            october_available = int(record[9])
            november_available = int(record[10])
            december_available = int(record[11])

            jan_other = int(jan_res) - january_available
            feb_other = int(feb_res) - february_available
            mar_other = int(mar_res) - march_available
            apr_other = int(apr_res) - april_available
            may_other = int(may_res) - may_available
            jun_other = int(jun_res) - june_available
            jul_other = int(jul_res) - july_available
            aug_other = int(aug_res) - august_available
            sep_other = int(sep_res) - september_available
            oct_other = int(oct_res) - october_available
            nov_other = int(nov_res) - november_available
            dec_other = int(dec_res) - december_available

            screens[15].ids.oth_1.text = str(jan_other)
            screens[15].ids.oth_2.text = str(feb_other)
            screens[15].ids.oth_3.text = str(mar_other)
            screens[15].ids.oth_4.text = str(apr_other)
            screens[15].ids.oth_5.text = str(may_other)
            screens[15].ids.oth_6.text = str(jun_other)
            screens[15].ids.oth_7.text = str(jul_other)
            screens[15].ids.oth_8.text = str(aug_other)
            screens[15].ids.oth_9.text = str(sep_other)
            screens[15].ids.oth_10.text = str(oct_other)
            screens[15].ids.oth_11.text = str(nov_other)
            screens[15].ids.oth_12.text = str(dec_other)

        conn.commit()
        conn.close()

        screens[15].show()

    @staticmethod
    def submit_cond():
        screens[3].submit_cond()
        screens[4].submit_cond()
        screens[5].submit_cond()
        screens[6].submit_cond()
        screens[7].submit_cond()
        screens[8].submit_cond()
        screens[9].submit_cond()
        screens[10].submit_cond()
        screens[11].submit_cond()
        screens[12].submit_cond()
        screens[13].submit_cond()
        screens[14].submit_cond()


# Building the Month Screens
class January(Screen):
    def submit(self):
        empty_fields_cond(self)
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("INSERT INTO january VALUES (:rent, :electricity, :heat, :water, :food, :building, "
                  ":internet, :goofy, :cigarettes, :credit, :additional)",
                  {'rent': self.ids.rent_input.text[0:4],
                   'electricity': self.ids.electricity_input.text[0:4],
                   'heat': self.ids.heat_input.text[0:4],
                   'water': self.ids.water_input.text[0:4],
                   'food': self.ids.food_input.text[0:4],
                   'building': self.ids.building_input.text[0:4],
                   'internet': self.ids.internet_input.text[0:4],
                   'goofy': self.ids.goofy_input.text[0:4],
                   'cigarettes': self.ids.cigarettes_input.text[0:4],
                   'credit': self.ids.credit_input.text[0:4],
                   'additional': self.ids.additional_input.text[0:4]})
        conn.commit()
        conn.close()

        self.cancel()
        self.show_total_paid()
        self.submit_cond()
        self.hide()
        self.show()

    def submit_cond(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM january where oid= 1")
        records = c.fetchall()
        for record in records:
            self.ids.rent_input.text = str(record[0])
            self.ids.electricity_input.text = str(record[1])
            self.ids.heat_input.text = str(record[2])
            self.ids.water_input.text = str(record[3])
            self.ids.food_input.text = str(record[4])
            self.ids.building_input.text = str(record[5])
            self.ids.internet_input.text = str(record[6])
            self.ids.goofy_input.text = str(record[7])
            self.ids.cigarettes_input.text = str(record[8])
            self.ids.credit_input.text = str(record[9])
            self.ids.additional_input.text = str(record[10])

        if self.ids.rent_input.text == "" and self.ids.electricity_input.text == "" and \
                self.ids.heat_input.text == "" and self.ids.water_input.text == "" and \
                self.ids.food_input.text == "" and self.ids.building_input.text == "" and \
                self.ids.internet_input.text == "" and self.ids.goofy_input.text == "" and \
                self.ids.cigarettes_input.text == "" and self.ids.credit_input.text == "" and \
                self.ids.additional_input.text == "":
            self.ids.submit.disabled = False
        else:
            self.ids.submit.disabled = True

        self.cancel()

        conn.commit()
        conn.close()

    def cancel(self):
        cancel(self)
        self.hide()

    def edit(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT * FROM january WHERE oid = 1")
        records = c.fetchall()
        for record in records:
            rent = str(record[0])
            self.ids.rent_input.text = rent
            electricity = str(record[1])
            self.ids.electricity_input.text = electricity
            heat = str(record[2])
            self.ids.heat_input.text = heat
            water = str(record[3])
            self.ids.water_input.text = water
            food = str(record[4])
            self.ids.food_input.text = food
            building = str(record[5])
            self.ids.building_input.text = building
            internet = str(record[6])
            self.ids.internet_input.text = internet
            goofy = str(record[7])
            self.ids.goofy_input.text = goofy
            cigarettes = str(record[8])
            self.ids.cigarettes_input.text = cigarettes
            credit = str(record[9])
            self.ids.credit_input.text = credit
            additional = str(record[10])
            self.ids.additional_input.text = additional
        conn.commit()
        conn.close()

        add_widgets_enable(self)

    def save(self):
        empty_fields_cond(self)
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("""UPDATE january SET
                                rent = :rent,
                                electricity = :electricity,
                                heat = :heat,
                                water = :water,
                                food = :food,
                                building = :building,
                                internet = :internet,
                                goofy = :goofy,
                                cigarettes = :cigarettes,
                                credit = :credit,
                                additional = :additional

                                WHERE oid = 1""", {
                   'rent': self.ids.rent_input.text[0:4],
                   'electricity': self.ids.electricity_input.text[0:4],
                   'heat': self.ids.heat_input.text[0:4],
                   'water': self.ids.water_input.text[0:4],
                   'food': self.ids.food_input.text[0:4],
                   'building': self.ids.building_input.text[0:4],
                   'internet': self.ids.internet_input.text[0:4],
                   'goofy': self.ids.goofy_input.text[0:4],
                   'cigarettes': self.ids.cigarettes_input.text[0:4],
                   'credit': self.ids.credit_input.text[0:4],
                   'additional': self.ids.additional_input.text[0:4]})
        conn.commit()
        conn.close()

        self.cancel()
        self.hide()
        self.show()
        self.show_total_paid()

    def show_total_paid(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM january where oid= 1")
        records = c.fetchall()
        for record in records:
            a = int(record[0])
            b = int(record[1])
            c = int(record[2])
            d = int(record[3])
            e = int(record[4])
            f = int(record[5])
            g = int(record[6])
            h = int(record[7])
            i = int(record[8])
            j = int(record[9])
            k = int(record[10])

            total = a + b + c + d + e + f + g + h + j + i + k
            me = a/2 + b/2 + c/2 + d/2 + e/2 + f/2 + g/2 + h/2 + i + j + k

            if int(self.ids.rent_check.active) == 0:
                total = total - a
                me = round(me - a/2)
            else:
                total = total
                me = round(me)
            if int(self.ids.electricity_check.active) == 0:
                total = total - b
                me = round(me - b/2)
            else:
                total = total
                me = round(me)
            if int(self.ids.heat_check.active) == 0:
                total = total - c
                me = round(me - c/2)
            else:
                total = total
                me = round(me)
            if int(self.ids.water_check.active) == 0:
                total = total - d
                me = round(me - d/2)
            else:
                total = total
                me = round(me)
            if int(self.ids.food_check.active) == 0:
                total = total - e
                me = round(me - e/2)
            else:
                total = total
                me = round(me)
            if int(self.ids.building_check.active) == 0:
                total = total - f
                me = round(me - f/2)
            else:
                total = total
                me = round(me)
            if int(self.ids.internet_check.active) == 0:
                total = total - g
                me = round(me - g/2)
            else:
                total = total
                me = round(me)
            if int(self.ids.goofy_check.active) == 0:
                total = total - h
                me = round(me - h/2)
            else:
                total = total
                me = round(me)
            if int(self.ids.cigarettes_check.active) == 0:
                total = total - i
                me = round(me - i)
            else:
                total = total
                me = round(me)
            if int(self.ids.credit_check.active) == 0:
                total = total - j
                me = round(me - j)
            else:
                total = total
                me = round(me)
            if int(self.ids.additional_check.active) == 0:
                total = total - k
                me = round(me - k)
            else:
                total = total
                me = round(me)

            self.ids.show_total_paid_1.text = "Total:"
            self.ids.show_total_paid_2.text = str(total)
            self.ids.show_total_paid_3.text = "For Me:"
            self.ids.show_total_paid_4.text = str(me)

        conn.commit()
        conn.close()

    def show(self):
        if self.ids.rent_paid.opacity == 0 and self.ids.rent_unpaid.opacity == 0:
            self.ids.show.text = 'Hide Table'
            self.ids.show_total_paid_1.text = "Total:"
            self.ids.show_total_paid_3.text = "For Me:"

            conn = sqlite3.connect('test.db')
            c = conn.cursor()
            c.execute("SELECT *, oid FROM january where oid= 1")
            records = c.fetchall()
            for record in records:
                rent = str(record[0])
                electricity = str(record[1])
                heat = str(record[2])
                water = str(record[3])
                food = str(record[4])
                building = str(record[5])
                internet = str(record[6])
                goofy = str(record[7])
                cigarettes = str(record[8])
                credit = str(record[9])
                additional = str(record[10])

                self.ids.rent_price.text = rent
                self.ids.electricity_price.text = electricity
                self.ids.heat_price.text = heat
                self.ids.water_price.text = water
                self.ids.food_price.text = food
                self.ids.building_price.text = building
                self.ids.internet_price.text = internet
                self.ids.goofy_price.text = goofy
                self.ids.cigarettes_price.text = cigarettes
                self.ids.credit_price.text = credit
                self.ids.additional_price.text = additional
            conn.commit()
            conn.close()

            show_rename_in_table(self)
            self.show_paid_unpaid()
            widgets_enable(self)
        else:
            self.ids.show.text = 'Show Table'
            self.hide()

    def hide(self):
        hide(self)

    def rename(self):
        self.hide()
        rename(self)

    def save_rename(self):
        save_rename(self)
        self.submit_cond()

    def delete(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("DELETE FROM january")
        conn.commit()
        conn.close()

        uncheck(self)
        delete_cond_reset(self)
        self.cancel()
        self.show_total_paid()
        self.submit_cond()
        self.hide()
        self.show()

    def delete_cond(self):
        delete_cond(self)

    def back(self):
        input_numbers(self)
        enable_other(self)
        self.cancel()
        self.hide()
        delete_cond_reset(self)

    def show_paid_unpaid(self):
        show_paid_unpaid(self)

    def add_function(self):
        add_function(self)

    @staticmethod
    def checkbox_state():
        save_checkbox_config()

    def remove_text_on_click(self):
        remove_text_on_click_rename(self)


class February(Screen):
    def submit(self):
        empty_fields_cond(self)
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("INSERT INTO february VALUES (:rent, :electricity, :heat, :water, :food, :building, "
                  ":internet, :goofy, :cigarettes, :credit, :additional)",
                  {'rent': self.ids.rent_input.text[0:4],
                   'electricity': self.ids.electricity_input.text[0:4],
                   'heat': self.ids.heat_input.text[0:4],
                   'water': self.ids.water_input.text[0:4],
                   'food': self.ids.food_input.text[0:4],
                   'building': self.ids.building_input.text[0:4],
                   'internet': self.ids.internet_input.text[0:4],
                   'goofy': self.ids.goofy_input.text[0:4],
                   'cigarettes': self.ids.cigarettes_input.text[0:4],
                   'credit': self.ids.credit_input.text[0:4],
                   'additional': self.ids.additional_input.text[0:4]})
        conn.commit()
        conn.close()

        self.cancel()
        self.show_total_paid()
        self.submit_cond()
        self.hide()
        self.show()

    def submit_cond(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM february where oid= 1")
        records = c.fetchall()
        for record in records:
            self.ids.rent_input.text = str(record[0])
            self.ids.electricity_input.text = str(record[1])
            self.ids.heat_input.text = str(record[2])
            self.ids.water_input.text = str(record[3])
            self.ids.food_input.text = str(record[4])
            self.ids.building_input.text = str(record[5])
            self.ids.internet_input.text = str(record[6])
            self.ids.goofy_input.text = str(record[7])
            self.ids.cigarettes_input.text = str(record[8])
            self.ids.credit_input.text = str(record[9])
            self.ids.additional_input.text = str(record[10])

        if self.ids.rent_input.text == "" and self.ids.electricity_input.text == "" and \
                self.ids.heat_input.text == "" and self.ids.water_input.text == "" and \
                self.ids.food_input.text == "" and self.ids.building_input.text == "" and \
                self.ids.internet_input.text == "" and self.ids.goofy_input.text == "" and \
                self.ids.cigarettes_input.text == "" and self.ids.credit_input.text == "" and \
                self.ids.additional_input.text == "":
            self.ids.submit.disabled = False
        else:
            self.ids.submit.disabled = True

        conn.commit()
        conn.close()

        self.cancel()

    def cancel(self):
        cancel(self)
        self.hide()

    def edit(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT * FROM february WHERE oid = 1")
        records = c.fetchall()
        for record in records:
            rent = str(record[0])
            self.ids.rent_input.text = rent
            electricity = str(record[1])
            self.ids.electricity_input.text = electricity
            heat = str(record[2])
            self.ids.heat_input.text = heat
            water = str(record[3])
            self.ids.water_input.text = water
            food = str(record[4])
            self.ids.food_input.text = food
            building = str(record[5])
            self.ids.building_input.text = building
            internet = str(record[6])
            self.ids.internet_input.text = internet
            goofy = str(record[7])
            self.ids.goofy_input.text = goofy
            cigarettes = str(record[8])
            self.ids.cigarettes_input.text = cigarettes
            credit = str(record[9])
            self.ids.credit_input.text = credit
            additional = str(record[10])
            self.ids.additional_input.text = additional
        conn.commit()
        conn.close()

        add_widgets_enable(self)

    def save(self):
        empty_fields_cond(self)
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("""UPDATE february SET
                                rent = :rent,
                                electricity = :electricity,
                                heat = :heat,
                                water = :water,
                                food = :food,
                                building = :building,
                                internet = :internet,
                                goofy = :goofy,
                                cigarettes = :cigarettes,
                                credit = :credit,
                                additional = :additional

                                WHERE oid = 1""", {
                   'rent': self.ids.rent_input.text[0:4],
                   'electricity': self.ids.electricity_input.text[0:4],
                   'heat': self.ids.heat_input.text[0:4],
                   'water': self.ids.water_input.text[0:4],
                   'food': self.ids.food_input.text[0:4],
                   'building': self.ids.building_input.text[0:4],
                   'internet': self.ids.internet_input.text[0:4],
                   'goofy': self.ids.goofy_input.text[0:4],
                   'cigarettes': self.ids.cigarettes_input.text[0:4],
                   'credit': self.ids.credit_input.text[0:4],
                   'additional': self.ids.additional_input.text[0:4]})
        conn.commit()
        conn.close()

        self.cancel()
        self.hide()
        self.show()
        self.show_total_paid()

    def show_total_paid(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM february where oid= 1")
        records = c.fetchall()
        for record in records:
            a = int(record[0])
            b = int(record[1])
            c = int(record[2])
            d = int(record[3])
            e = int(record[4])
            f = int(record[5])
            g = int(record[6])
            h = int(record[7])
            i = int(record[8])
            j = int(record[9])
            k = int(record[10])

            total = a + b + c + d + e + f + g + h + i + j + k
            me = a/2 + b/2 + c/2 + d/2 + e/2 + f/2 + g/2 + h/2 + i + j + k

            if int(self.ids.rent_check.active) == 0:
                total = total - a
                me = round(me - a/2)
            else:
                total = total
                round(me)
            if int(self.ids.electricity_check.active) == 0:
                total = total - b
                me = round(me - b/2)
            else:
                total = total
                me = round(me)
            if int(self.ids.heat_check.active) == 0:
                total = total - c
                me = round(me - c/2)
            else:
                total = total
                me = round(me)
            if int(self.ids.water_check.active) == 0:
                total = total - d
                me = round(me - d/2)
            else:
                total = total
                me = round(me)
            if int(self.ids.food_check.active) == 0:
                total = total - e
                me = round(me - e/2)
            else:
                total = total
                me = round(me)
            if int(self.ids.building_check.active) == 0:
                total = total - f
                me = round(me - f/2)
            else:
                total = total
                me = round(me)
            if int(self.ids.internet_check.active) == 0:
                total = total - g
                me = round(me - g/2)
            else:
                total = total
                me = round(me)
            if int(self.ids.goofy_check.active) == 0:
                total = total - h
                me = round(me - h/2)
            else:
                total = total
                me = round(me)
            if int(self.ids.cigarettes_check.active) == 0:
                total = total - i
                me = round(me - i)
            else:
                total = total
                me = round(me)
            if int(self.ids.credit_check.active) == 0:
                total = total - j
                me = round(me - j)
            else:
                total = total
                me = round(me)
            if int(self.ids.additional_check.active) == 0:
                total = total - k
                me = round(me - k)
            else:
                total = total
                me = round(me)

            self.ids.show_total_paid_1.text = "Total:"
            self.ids.show_total_paid_2.text = str(total)
            self.ids.show_total_paid_3.text = "For Me:"
            self.ids.show_total_paid_4.text = str(me)

        conn.commit()
        conn.close()

    def show(self):
        if self.ids.rent_paid.opacity == 0 and self.ids.rent_unpaid.opacity == 0:
            self.ids.show.text = 'Hide Table'
            self.ids.show_total_paid_1.text = "Total:"
            self.ids.show_total_paid_3.text = "For Me:"

            conn = sqlite3.connect('test.db')
            c = conn.cursor()
            c.execute("SELECT *, oid FROM february where oid= 1")
            records = c.fetchall()
            for record in records:
                rent = str(record[0])
                electricity = str(record[1])
                heat = str(record[2])
                water = str(record[3])
                food = str(record[4])
                building = str(record[5])
                internet = str(record[6])
                goofy = str(record[7])
                cigarettes = str(record[8])
                credit = str(record[9])
                additional = str(record[10])

                self.ids.rent_price.text = rent
                self.ids.electricity_price.text = electricity
                self.ids.heat_price.text = heat
                self.ids.water_price.text = water
                self.ids.food_price.text = food
                self.ids.building_price.text = building
                self.ids.internet_price.text = internet
                self.ids.goofy_price.text = goofy
                self.ids.cigarettes_price.text = cigarettes
                self.ids.credit_price.text = credit
                self.ids.additional_price.text = additional
            conn.commit()
            conn.close()

            show_rename_in_table(self)
            self.show_paid_unpaid()
            widgets_enable(self)
        else:
            self.ids.show.text = 'Show Table'
            self.hide()

    def hide(self):
        hide(self)

    def rename(self):
        self.hide()
        rename(self)

    def save_rename(self):
        save_rename(self)
        self.submit_cond()

    def delete(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("DELETE FROM february")
        conn.commit()
        conn.close()

        uncheck(self)
        delete_cond_reset(self)
        self.cancel()
        self.show_total_paid()
        self.submit_cond()
        self.hide()
        self.show()

    def delete_cond(self):
        delete_cond(self)

    def back(self):
        input_numbers(self)
        enable_other(self)
        self.cancel()
        self.hide()
        delete_cond_reset(self)

    def show_paid_unpaid(self):
        show_paid_unpaid(self)

    def add_function(self):
        add_function(self)

    @staticmethod
    def checkbox_state():
        save_checkbox_config()

    def remove_text_on_click(self):
        remove_text_on_click_rename(self)


class March(Screen):
    def submit(self):
        empty_fields_cond(self)
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("INSERT INTO march VALUES (:rent, :electricity, :heat, :water, :food, :building, "
                  ":internet, :goofy, :cigarettes, :credit, :additional)",
                  {'rent': self.ids.rent_input.text[0:4],
                   'electricity': self.ids.electricity_input.text[0:4],
                   'heat': self.ids.heat_input.text[0:4],
                   'water': self.ids.water_input.text[0:4],
                   'food': self.ids.food_input.text[0:4],
                   'building': self.ids.building_input.text[0:4],
                   'internet': self.ids.internet_input.text[0:4],
                   'goofy': self.ids.goofy_input.text[0:4],
                   'cigarettes': self.ids.cigarettes_input.text[0:4],
                   'credit': self.ids.credit_input.text[0:4],
                   'additional': self.ids.additional_input.text[0:4]})
        conn.commit()
        conn.close()

        self.cancel()
        self.show_total_paid()
        self.submit_cond()
        self.hide()
        self.show()

    def submit_cond(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM march where oid= 1")
        records = c.fetchall()
        for record in records:
            self.ids.rent_input.text = str(record[0])
            self.ids.electricity_input.text = str(record[1])
            self.ids.heat_input.text = str(record[2])
            self.ids.water_input.text = str(record[3])
            self.ids.food_input.text = str(record[4])
            self.ids.building_input.text = str(record[5])
            self.ids.internet_input.text = str(record[6])
            self.ids.goofy_input.text = str(record[7])
            self.ids.cigarettes_input.text = str(record[8])
            self.ids.credit_input.text = str(record[9])
            self.ids.additional_input.text = str(record[10])

        if self.ids.rent_input.text == "" and self.ids.electricity_input.text == "" and \
                self.ids.heat_input.text == "" and self.ids.water_input.text == "" and \
                self.ids.food_input.text == "" and self.ids.building_input.text == "" and \
                self.ids.internet_input.text == "" and self.ids.goofy_input.text == "" and \
                self.ids.cigarettes_input.text == "" and self.ids.credit_input.text == "" and \
                self.ids.additional_input.text == "":
            self.ids.submit.disabled = False
        else:
            self.ids.submit.disabled = True

        self.cancel()

        conn.commit()
        conn.close()

    def cancel(self):
        cancel(self)
        self.hide()

    def edit(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT * FROM march WHERE oid = 1")
        records = c.fetchall()
        for record in records:
            rent = str(record[0])
            self.ids.rent_input.text = rent
            electricity = str(record[1])
            self.ids.electricity_input.text = electricity
            heat = str(record[2])
            self.ids.heat_input.text = heat
            water = str(record[3])
            self.ids.water_input.text = water
            food = str(record[4])
            self.ids.food_input.text = food
            building = str(record[5])
            self.ids.building_input.text = building
            internet = str(record[6])
            self.ids.internet_input.text = internet
            goofy = str(record[7])
            self.ids.goofy_input.text = goofy
            cigarettes = str(record[8])
            self.ids.cigarettes_input.text = cigarettes
            credit = str(record[9])
            self.ids.credit_input.text = credit
            additional = str(record[10])
            self.ids.additional_input.text = additional
        conn.commit()
        conn.close()

        add_widgets_enable(self)

    def save(self):
        empty_fields_cond(self)
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("""UPDATE march SET
                                rent = :rent,
                                electricity = :electricity,
                                heat = :heat,
                                water = :water,
                                food = :food,
                                building = :building,
                                internet = :internet,
                                goofy = :goofy,
                                cigarettes = :cigarettes,
                                credit = :credit,
                                additional = :additional

                                WHERE oid = 1""", {
                   'rent': self.ids.rent_input.text[0:4],
                   'electricity': self.ids.electricity_input.text[0:4],
                   'heat': self.ids.heat_input.text[0:4],
                   'water': self.ids.water_input.text[0:4],
                   'food': self.ids.food_input.text[0:4],
                   'building': self.ids.building_input.text[0:4],
                   'internet': self.ids.internet_input.text[0:4],
                   'goofy': self.ids.goofy_input.text[0:4],
                   'cigarettes': self.ids.cigarettes_input.text[0:4],
                   'credit': self.ids.credit_input.text[0:4],
                   'additional': self.ids.additional_input.text[0:4]})
        conn.commit()
        conn.close()

        self.cancel()
        self.hide()
        self.show()
        self.show_total_paid()

    def show_total_paid(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM march where oid= 1")
        records = c.fetchall()
        for record in records:
            a = int(record[0])
            b = int(record[1])
            c = int(record[2])
            d = int(record[3])
            e = int(record[4])
            f = int(record[5])
            g = int(record[6])
            h = int(record[7])
            i = int(record[8])
            j = int(record[9])
            k = int(record[10])

            total = a + b + c + d + e + f + g + h + i + j + k
            me = a/2 + b/2 + c/2 + d/2 + e/2 + f/2 + g/2 + h/2 + i + j + k

            if int(self.ids.rent_check.active) == 0:
                total = total - a
                me = round(me - a/2)
            else:
                total = total
                me = round(me)
            if int(self.ids.electricity_check.active) == 0:
                total = total - b
                me = round(me - b/2)
            else:
                total = total
                me = round(me)
            if int(self.ids.heat_check.active) == 0:
                total = total - c
                me = round(me - c/2)
            else:
                total = total
                me = round(me)
            if int(self.ids.water_check.active) == 0:
                total = total - d
                me = round(me - d/2)
            else:
                total = total
                me = round(me)
            if int(self.ids.food_check.active) == 0:
                total = total - e
                me = round(me - e/2)
            else:
                total = total
                me = round(me)
            if int(self.ids.building_check.active) == 0:
                total = total - f
                me = round(me - f/2)
            else:
                total = total
                me = round(me)
            if int(self.ids.internet_check.active) == 0:
                total = total - g
                me = round(me - g/2)
            else:
                total = total
                me = round(me)
            if int(self.ids.goofy_check.active) == 0:
                total = total - h
                me = round(me - h/2)
            else:
                total = total
                me = round(me)
            if int(self.ids.cigarettes_check.active) == 0:
                total = total - i
                me = round(me - i)
            else:
                total = total
                me = round(me)
            if int(self.ids.credit_check.active) == 0:
                total = total - j
                me = round(me - j)
            else:
                total = total
                me = round(me)
            if int(self.ids.additional_check.active) == 0:
                total = total - k
                me = round(me - k)
            else:
                total = total
                me = round(me)

            self.ids.show_total_paid_1.text = "Total:"
            self.ids.show_total_paid_2.text = str(total)
            self.ids.show_total_paid_3.text = "For Me:"
            self.ids.show_total_paid_4.text = str(me)

        conn.commit()
        conn.close()

    def show(self):
        if self.ids.rent_paid.opacity == 0 and self.ids.rent_unpaid.opacity == 0:
            self.ids.show.text = 'Hide Table'
            self.ids.show_total_paid_1.text = "Total:"
            self.ids.show_total_paid_3.text = "For Me:"

            conn = sqlite3.connect('test.db')
            c = conn.cursor()
            c.execute("SELECT *, oid FROM march where oid= 1")
            records = c.fetchall()
            for record in records:
                rent = str(record[0])
                electricity = str(record[1])
                heat = str(record[2])
                water = str(record[3])
                food = str(record[4])
                building = str(record[5])
                internet = str(record[6])
                goofy = str(record[7])
                cigarettes = str(record[8])
                credit = str(record[9])
                additional = str(record[10])

                self.ids.rent_price.text = rent
                self.ids.electricity_price.text = electricity
                self.ids.heat_price.text = heat
                self.ids.water_price.text = water
                self.ids.food_price.text = food
                self.ids.building_price.text = building
                self.ids.internet_price.text = internet
                self.ids.goofy_price.text = goofy
                self.ids.cigarettes_price.text = cigarettes
                self.ids.credit_price.text = credit
                self.ids.additional_price.text = additional
            conn.commit()
            conn.close()

            show_rename_in_table(self)
            self.show_paid_unpaid()
            widgets_enable(self)
        else:
            self.ids.show.text = 'Show Table'
            self.hide()

    def hide(self):
        hide(self)

    def rename(self):
        self.hide()
        rename(self)

    def save_rename(self):
        save_rename(self)
        self.submit_cond()

    def delete(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("DELETE FROM march")
        conn.commit()
        conn.close()

        uncheck(self)
        delete_cond_reset(self)
        self.cancel()
        self.show_total_paid()
        self.submit_cond()
        self.hide()
        self.show()

    def delete_cond(self):
        delete_cond(self)

    def back(self):
        input_numbers(self)
        enable_other(self)
        self.cancel()
        self.hide()
        delete_cond_reset(self)

    def show_paid_unpaid(self):
        show_paid_unpaid(self)

    def add_function(self):
        add_function(self)

    @staticmethod
    def checkbox_state():
        save_checkbox_config()

    def remove_text_on_click(self):
        remove_text_on_click_rename(self)


class April(Screen):
    def submit(self):
        empty_fields_cond(self)
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("INSERT INTO april VALUES (:rent, :electricity, :heat, :water, :food, :building, "
                  ":internet, :goofy, :cigarettes, :credit, :additional)",
                  {'rent': self.ids.rent_input.text[0:4],
                   'electricity': self.ids.electricity_input.text[0:4],
                   'heat': self.ids.heat_input.text[0:4],
                   'water': self.ids.water_input.text[0:4],
                   'food': self.ids.food_input.text[0:4],
                   'building': self.ids.building_input.text[0:4],
                   'internet': self.ids.internet_input.text[0:4],
                   'goofy': self.ids.goofy_input.text[0:4],
                   'cigarettes': self.ids.cigarettes_input.text[0:4],
                   'credit': self.ids.credit_input.text[0:4],
                   'additional': self.ids.additional_input.text[0:4]})
        conn.commit()
        conn.close()

        self.cancel()
        self.show_total_paid()
        self.submit_cond()
        self.hide()
        self.show()

    def submit_cond(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM april where oid= 1")
        records = c.fetchall()
        for record in records:
            self.ids.rent_input.text = str(record[0])
            self.ids.electricity_input.text = str(record[1])
            self.ids.heat_input.text = str(record[2])
            self.ids.water_input.text = str(record[3])
            self.ids.food_input.text = str(record[4])
            self.ids.building_input.text = str(record[5])
            self.ids.internet_input.text = str(record[6])
            self.ids.goofy_input.text = str(record[7])
            self.ids.cigarettes_input.text = str(record[8])
            self.ids.credit_input.text = str(record[9])
            self.ids.additional_input.text = str(record[10])

        if self.ids.rent_input.text == "" and self.ids.electricity_input.text == "" and \
                self.ids.heat_input.text == "" and self.ids.water_input.text == "" and \
                self.ids.food_input.text == "" and self.ids.building_input.text == "" and \
                self.ids.internet_input.text == "" and self.ids.goofy_input.text == "" and \
                self.ids.cigarettes_input.text == "" and self.ids.credit_input.text == "" and \
                self.ids.additional_input.text == "":
            self.ids.submit.disabled = False
        else:
            self.ids.submit.disabled = True

        self.cancel()

        conn.commit()
        conn.close()

    def cancel(self):
        cancel(self)
        self.hide()

    def edit(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT * FROM april WHERE oid = 1")
        records = c.fetchall()
        for record in records:
            rent = str(record[0])
            self.ids.rent_input.text = rent
            electricity = str(record[1])
            self.ids.electricity_input.text = electricity
            heat = str(record[2])
            self.ids.heat_input.text = heat
            water = str(record[3])
            self.ids.water_input.text = water
            food = str(record[4])
            self.ids.food_input.text = food
            building = str(record[5])
            self.ids.building_input.text = building
            internet = str(record[6])
            self.ids.internet_input.text = internet
            goofy = str(record[7])
            self.ids.goofy_input.text = goofy
            cigarettes = str(record[8])
            self.ids.cigarettes_input.text = cigarettes
            credit = str(record[9])
            self.ids.credit_input.text = credit
            additional = str(record[10])
            self.ids.additional_input.text = additional
        conn.commit()
        conn.close()

        add_widgets_enable(self)

    def save(self):
        empty_fields_cond(self)
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("""UPDATE april SET
                                rent = :rent,
                                electricity = :electricity,
                                heat = :heat,
                                water = :water,
                                food = :food,
                                building = :building,
                                internet = :internet,
                                goofy = :goofy,
                                cigarettes = :cigarettes,
                                credit = :credit,
                                additional = :additional

                                WHERE oid = 1""", {
                   'rent': self.ids.rent_input.text[0:4],
                   'electricity': self.ids.electricity_input.text[0:4],
                   'heat': self.ids.heat_input.text[0:4],
                   'water': self.ids.water_input.text[0:4],
                   'food': self.ids.food_input.text[0:4],
                   'building': self.ids.building_input.text[0:4],
                   'internet': self.ids.internet_input.text[0:4],
                   'goofy': self.ids.goofy_input.text[0:4],
                   'cigarettes': self.ids.cigarettes_input.text[0:4],
                   'credit': self.ids.credit_input.text[0:4],
                   'additional': self.ids.additional_input.text[0:4]})
        conn.commit()
        conn.close()

        self.cancel()
        self.hide()
        self.show()
        self.show_total_paid()

    def show_total_paid(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM april where oid= 1")
        records = c.fetchall()
        for record in records:
            a = int(record[0])
            b = int(record[1])
            c = int(record[2])
            d = int(record[3])
            e = int(record[4])
            f = int(record[5])
            g = int(record[6])
            h = int(record[7])
            i = int(record[8])
            j = int(record[9])
            k = int(record[10])

            total = a + b + c + d + e + f + g + h + i + j + k
            me = a / 2 + b / 2 + c / 2 + d / 2 + e / 2 + f / 2 + g / 2 + h / 2 + i + j + k

            if int(self.ids.rent_check.active) == 0:
                total = total - a
                me = round(me - a / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.electricity_check.active) == 0:
                total = total - b
                me = round(me - b / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.heat_check.active) == 0:
                total = total - c
                me = round(me - c / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.water_check.active) == 0:
                total = total - d
                me = round(me - d / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.food_check.active) == 0:
                total = total - e
                me = round(me - e / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.building_check.active) == 0:
                total = total - f
                me = round(me - f / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.internet_check.active) == 0:
                total = total - g
                me = round(me - g / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.goofy_check.active) == 0:
                total = total - h
                me = round(me - h / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.cigarettes_check.active) == 0:
                total = total - i
                me = round(me - i)
            else:
                total = total
                me = round(me)
            if int(self.ids.credit_check.active) == 0:
                total = total - j
                me = round(me - j)
            else:
                total = total
                me = round(me)
            if int(self.ids.additional_check.active) == 0:
                total = total - k
                me = round(me - k)
            else:
                total = total
                me = round(me)

            self.ids.show_total_paid_1.text = "Total:"
            self.ids.show_total_paid_2.text = str(total)
            self.ids.show_total_paid_3.text = "For Me:"
            self.ids.show_total_paid_4.text = str(me)

        conn.commit()
        conn.close()

    def show(self):
        if self.ids.rent_paid.opacity == 0 and self.ids.rent_unpaid.opacity == 0:
            self.ids.show.text = 'Hide Table'
            self.ids.show_total_paid_1.text = "Total:"
            self.ids.show_total_paid_3.text = "For Me:"

            conn = sqlite3.connect('test.db')
            c = conn.cursor()
            c.execute("SELECT *, oid FROM april where oid= 1")
            records = c.fetchall()
            for record in records:
                rent = str(record[0])
                electricity = str(record[1])
                heat = str(record[2])
                water = str(record[3])
                food = str(record[4])
                building = str(record[5])
                internet = str(record[6])
                goofy = str(record[7])
                cigarettes = str(record[8])
                credit = str(record[9])
                additional = str(record[10])

                self.ids.rent_price.text = rent
                self.ids.electricity_price.text = electricity
                self.ids.heat_price.text = heat
                self.ids.water_price.text = water
                self.ids.food_price.text = food
                self.ids.building_price.text = building
                self.ids.internet_price.text = internet
                self.ids.goofy_price.text = goofy
                self.ids.cigarettes_price.text = cigarettes
                self.ids.credit_price.text = credit
                self.ids.additional_price.text = additional
            conn.commit()
            conn.close()

            show_rename_in_table(self)
            self.show_paid_unpaid()
            widgets_enable(self)
        else:
            self.ids.show.text = 'Show Table'
            self.hide()

    def hide(self):
        hide(self)

    def rename(self):
        self.hide()
        rename(self)

    def save_rename(self):
        save_rename(self)
        self.submit_cond()

    def delete(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("DELETE FROM april")
        conn.commit()
        conn.close()

        uncheck(self)
        delete_cond_reset(self)
        self.cancel()
        self.show_total_paid()
        self.submit_cond()
        self.hide()
        self.show()

    def delete_cond(self):
        delete_cond(self)

    def back(self):
        input_numbers(self)
        enable_other(self)
        self.cancel()
        self.hide()
        delete_cond_reset(self)

    def show_paid_unpaid(self):
        show_paid_unpaid(self)

    def add_function(self):
        add_function(self)

    @staticmethod
    def checkbox_state():
        save_checkbox_config()

    def remove_text_on_click(self):
        remove_text_on_click_rename(self)


class May(Screen):
    def submit(self):
        empty_fields_cond(self)
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("INSERT INTO may VALUES (:rent, :electricity, :heat, :water, :food, :building, "
                  ":internet, :goofy, :cigarettes, :credit, :additional)",
                  {'rent': self.ids.rent_input.text[0:4],
                   'electricity': self.ids.electricity_input.text[0:4],
                   'heat': self.ids.heat_input.text[0:4],
                   'water': self.ids.water_input.text[0:4],
                   'food': self.ids.food_input.text[0:4],
                   'building': self.ids.building_input.text[0:4],
                   'internet': self.ids.internet_input.text[0:4],
                   'goofy': self.ids.goofy_input.text[0:4],
                   'cigarettes': self.ids.cigarettes_input.text[0:4],
                   'credit': self.ids.credit_input.text[0:4],
                   'additional': self.ids.additional_input.text[0:4]})
        conn.commit()
        conn.close()

        self.cancel()
        self.show_total_paid()
        self.submit_cond()
        self.hide()
        self.show()

    def submit_cond(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM may where oid= 1")
        records = c.fetchall()
        for record in records:
            self.ids.rent_input.text = str(record[0])
            self.ids.electricity_input.text = str(record[1])
            self.ids.heat_input.text = str(record[2])
            self.ids.water_input.text = str(record[3])
            self.ids.food_input.text = str(record[4])
            self.ids.building_input.text = str(record[5])
            self.ids.internet_input.text = str(record[6])
            self.ids.goofy_input.text = str(record[7])
            self.ids.cigarettes_input.text = str(record[8])
            self.ids.credit_input.text = str(record[9])
            self.ids.additional_input.text = str(record[10])

        if self.ids.rent_input.text == "" and self.ids.electricity_input.text == "" and \
                self.ids.heat_input.text == "" and self.ids.water_input.text == "" and \
                self.ids.food_input.text == "" and self.ids.building_input.text == "" and \
                self.ids.internet_input.text == "" and self.ids.goofy_input.text == "" and \
                self.ids.cigarettes_input.text == "" and self.ids.credit_input.text == "" and \
                self.ids.additional_input.text == "":
            self.ids.submit.disabled = False
        else:
            self.ids.submit.disabled = True

        self.cancel()

        conn.commit()
        conn.close()

    def cancel(self):
        cancel(self)
        self.hide()

    def edit(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT * FROM may WHERE oid = 1")
        records = c.fetchall()
        for record in records:
            rent = str(record[0])
            self.ids.rent_input.text = rent
            electricity = str(record[1])
            self.ids.electricity_input.text = electricity
            heat = str(record[2])
            self.ids.heat_input.text = heat
            water = str(record[3])
            self.ids.water_input.text = water
            food = str(record[4])
            self.ids.food_input.text = food
            building = str(record[5])
            self.ids.building_input.text = building
            internet = str(record[6])
            self.ids.internet_input.text = internet
            goofy = str(record[7])
            self.ids.goofy_input.text = goofy
            cigarettes = str(record[8])
            self.ids.cigarettes_input.text = cigarettes
            credit = str(record[9])
            self.ids.credit_input.text = credit
            additional = str(record[10])
            self.ids.additional_input.text = additional
        conn.commit()
        conn.close()

        add_widgets_enable(self)

    def save(self):
        empty_fields_cond(self)
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("""UPDATE may SET
                                rent = :rent,
                                electricity = :electricity,
                                heat = :heat,
                                water = :water,
                                food = :food,
                                building = :building,
                                internet = :internet,
                                goofy = :goofy,
                                cigarettes = :cigarettes,
                                credit = :credit,
                                additional = :additional

                                WHERE oid = 1""", {
                   'rent': self.ids.rent_input.text[0:4],
                   'electricity': self.ids.electricity_input.text[0:4],
                   'heat': self.ids.heat_input.text[0:4],
                   'water': self.ids.water_input.text[0:4],
                   'food': self.ids.food_input.text[0:4],
                   'building': self.ids.building_input.text[0:4],
                   'internet': self.ids.internet_input.text[0:4],
                   'goofy': self.ids.goofy_input.text[0:4],
                   'cigarettes': self.ids.cigarettes_input.text[0:4],
                   'credit': self.ids.credit_input.text[0:4],
                   'additional': self.ids.additional_input.text[0:4]})
        conn.commit()
        conn.close()

        self.cancel()
        self.hide()
        self.show()
        self.show_total_paid()

    def show_total_paid(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM may where oid= 1")
        records = c.fetchall()
        for record in records:
            a = int(record[0])
            b = int(record[1])
            c = int(record[2])
            d = int(record[3])
            e = int(record[4])
            f = int(record[5])
            g = int(record[6])
            h = int(record[7])
            i = int(record[8])
            j = int(record[9])
            k = int(record[10])

            total = a + b + c + d + e + f + g + h + i + j + k
            me = a / 2 + b / 2 + c / 2 + d / 2 + e / 2 + f / 2 + g / 2 + h / 2 + i + j + k

            if int(self.ids.rent_check.active) == 0:
                total = total - a
                me = round(me - a / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.electricity_check.active) == 0:
                total = total - b
                me = round(me - b / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.heat_check.active) == 0:
                total = total - c
                me = round(me - c / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.water_check.active) == 0:
                total = total - d
                me = round(me - d / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.food_check.active) == 0:
                total = total - e
                me = round(me - e / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.building_check.active) == 0:
                total = total - f
                me = round(me - f / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.internet_check.active) == 0:
                total = total - g
                me = round(me - g / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.goofy_check.active) == 0:
                total = total - h
                me = round(me - h / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.cigarettes_check.active) == 0:
                total = total - i
                me = round(me - i)
            else:
                total = total
                me = round(me)
            if int(self.ids.credit_check.active) == 0:
                total = total - j
                me = round(me - j)
            else:
                total = total
                me = round(me)
            if int(self.ids.additional_check.active) == 0:
                total = total - k
                me = round(me - k)
            else:
                total = total
                me = round(me)

            self.ids.show_total_paid_1.text = "Total:"
            self.ids.show_total_paid_2.text = str(total)
            self.ids.show_total_paid_3.text = "For Me:"
            self.ids.show_total_paid_4.text = str(me)

        conn.commit()
        conn.close()

    def show(self):
        if self.ids.rent_paid.opacity == 0 and self.ids.rent_unpaid.opacity == 0:
            self.ids.show.text = 'Hide Table'
            self.ids.show_total_paid_1.text = "Total:"
            self.ids.show_total_paid_3.text = "For Me:"

            conn = sqlite3.connect('test.db')
            c = conn.cursor()
            c.execute("SELECT *, oid FROM may where oid= 1")
            records = c.fetchall()
            for record in records:
                rent = str(record[0])
                electricity = str(record[1])
                heat = str(record[2])
                water = str(record[3])
                food = str(record[4])
                building = str(record[5])
                internet = str(record[6])
                goofy = str(record[7])
                cigarettes = str(record[8])
                credit = str(record[9])
                additional = str(record[10])

                self.ids.rent_price.text = rent
                self.ids.electricity_price.text = electricity
                self.ids.heat_price.text = heat
                self.ids.water_price.text = water
                self.ids.food_price.text = food
                self.ids.building_price.text = building
                self.ids.internet_price.text = internet
                self.ids.goofy_price.text = goofy
                self.ids.cigarettes_price.text = cigarettes
                self.ids.credit_price.text = credit
                self.ids.additional_price.text = additional
            conn.commit()
            conn.close()

            show_rename_in_table(self)
            self.show_paid_unpaid()
            widgets_enable(self)
        else:
            self.ids.show.text = 'Show Table'
            self.hide()

    def hide(self):
        hide(self)

    def rename(self):
        self.hide()
        rename(self)

    def save_rename(self):
        save_rename(self)
        self.submit_cond()

    def delete(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("DELETE FROM may")
        conn.commit()
        conn.close()

        uncheck(self)
        delete_cond_reset(self)
        self.cancel()
        self.show_total_paid()
        self.submit_cond()
        self.hide()
        self.show()

    def delete_cond(self):
        delete_cond(self)

    def back(self):
        input_numbers(self)
        enable_other(self)
        self.cancel()
        self.hide()
        delete_cond_reset(self)

    def show_paid_unpaid(self):
        show_paid_unpaid(self)

    def add_function(self):
        add_function(self)

    @staticmethod
    def checkbox_state():
        save_checkbox_config()

    def remove_text_on_click(self):
        remove_text_on_click_rename(self)


class June(Screen):
    def submit(self):
        empty_fields_cond(self)
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("INSERT INTO june VALUES (:rent, :electricity, :heat, :water, :food, :building, "
                  ":internet, :goofy, :cigarettes, :credit, :additional)",
                  {'rent': self.ids.rent_input.text[0:4],
                   'electricity': self.ids.electricity_input.text[0:4],
                   'heat': self.ids.heat_input.text[0:4],
                   'water': self.ids.water_input.text[0:4],
                   'food': self.ids.food_input.text[0:4],
                   'building': self.ids.building_input.text[0:4],
                   'internet': self.ids.internet_input.text[0:4],
                   'goofy': self.ids.goofy_input.text[0:4],
                   'cigarettes': self.ids.cigarettes_input.text[0:4],
                   'credit': self.ids.credit_input.text[0:4],
                   'additional': self.ids.additional_input.text[0:4]})
        conn.commit()
        conn.close()

        self.cancel()
        self.show_total_paid()
        self.submit_cond()
        self.hide()
        self.show()

    def submit_cond(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM june where oid= 1")
        records = c.fetchall()
        for record in records:
            self.ids.rent_input.text = str(record[0])
            self.ids.electricity_input.text = str(record[1])
            self.ids.heat_input.text = str(record[2])
            self.ids.water_input.text = str(record[3])
            self.ids.food_input.text = str(record[4])
            self.ids.building_input.text = str(record[5])
            self.ids.internet_input.text = str(record[6])
            self.ids.goofy_input.text = str(record[7])
            self.ids.cigarettes_input.text = str(record[8])
            self.ids.credit_input.text = str(record[9])
            self.ids.additional_input.text = str(record[10])

        if self.ids.rent_input.text == "" and self.ids.electricity_input.text == "" and \
                self.ids.heat_input.text == "" and self.ids.water_input.text == "" and \
                self.ids.food_input.text == "" and self.ids.building_input.text == "" and \
                self.ids.internet_input.text == "" and self.ids.goofy_input.text == "" and \
                self.ids.cigarettes_input.text == "" and self.ids.credit_input.text == "" and \
                self.ids.additional_input.text == "":
            self.ids.submit.disabled = False
        else:
            self.ids.submit.disabled = True

        self.cancel()

        conn.commit()
        conn.close()

    def cancel(self):
        cancel(self)
        self.hide()

    def edit(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT * FROM june WHERE oid = 1")
        records = c.fetchall()
        for record in records:
            rent = str(record[0])
            self.ids.rent_input.text = rent
            electricity = str(record[1])
            self.ids.electricity_input.text = electricity
            heat = str(record[2])
            self.ids.heat_input.text = heat
            water = str(record[3])
            self.ids.water_input.text = water
            food = str(record[4])
            self.ids.food_input.text = food
            building = str(record[5])
            self.ids.building_input.text = building
            internet = str(record[6])
            self.ids.internet_input.text = internet
            goofy = str(record[7])
            self.ids.goofy_input.text = goofy
            cigarettes = str(record[8])
            self.ids.cigarettes_input.text = cigarettes
            credit = str(record[9])
            self.ids.credit_input.text = credit
            additional = str(record[10])
            self.ids.additional_input.text = additional
        conn.commit()
        conn.close()

        add_widgets_enable(self)

    def save(self):
        empty_fields_cond(self)
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("""UPDATE june SET
                                rent = :rent,
                                electricity = :electricity,
                                heat = :heat,
                                water = :water,
                                food = :food,
                                building = :building,
                                internet = :internet,
                                goofy = :goofy,
                                cigarettes = :cigarettes,
                                credit = :credit,
                                additional = :additional

                                WHERE oid = 1""", {
                   'rent': self.ids.rent_input.text[0:4],
                   'electricity': self.ids.electricity_input.text[0:4],
                   'heat': self.ids.heat_input.text[0:4],
                   'water': self.ids.water_input.text[0:4],
                   'food': self.ids.food_input.text[0:4],
                   'building': self.ids.building_input.text[0:4],
                   'internet': self.ids.internet_input.text[0:4],
                   'goofy': self.ids.goofy_input.text[0:4],
                   'cigarettes': self.ids.cigarettes_input.text[0:4],
                   'credit': self.ids.credit_input.text[0:4],
                   'additional': self.ids.additional_input.text[0:4]})
        conn.commit()
        conn.close()

        self.cancel()
        self.hide()
        self.show()
        self.show_total_paid()

    def show_total_paid(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM june where oid= 1")
        records = c.fetchall()
        for record in records:
            a = int(record[0])
            b = int(record[1])
            c = int(record[2])
            d = int(record[3])
            e = int(record[4])
            f = int(record[5])
            g = int(record[6])
            h = int(record[7])
            i = int(record[8])
            j = int(record[9])
            k = int(record[10])

            total = a + b + c + d + e + f + g + h + i + j + k
            me = a / 2 + b / 2 + c / 2 + d / 2 + e / 2 + f / 2 + g / 2 + h / 2 + i + j + k

            if int(self.ids.rent_check.active) == 0:
                total = total - a
                me = round(me - a / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.electricity_check.active) == 0:
                total = total - b
                me = round(me - b / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.heat_check.active) == 0:
                total = total - c
                me = round(me - c / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.water_check.active) == 0:
                total = total - d
                me = round(me - d / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.food_check.active) == 0:
                total = total - e
                me = round(me - e / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.building_check.active) == 0:
                total = total - f
                me = round(me - f / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.internet_check.active) == 0:
                total = total - g
                me = round(me - g / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.goofy_check.active) == 0:
                total = total - h
                me = round(me - h / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.cigarettes_check.active) == 0:
                total = total - i
                me = round(me - i)
            else:
                total = total
                me = round(me)
            if int(self.ids.credit_check.active) == 0:
                total = total - j
                me = round(me - j)
            else:
                total = total
                me = round(me)
            if int(self.ids.additional_check.active) == 0:
                total = total - k
                me = round(me - k)
            else:
                total = total
                me = round(me)

            self.ids.show_total_paid_1.text = "Total:"
            self.ids.show_total_paid_2.text = str(total)
            self.ids.show_total_paid_3.text = "For Me:"
            self.ids.show_total_paid_4.text = str(me)

        conn.commit()
        conn.close()

    def show(self):
        if self.ids.rent_paid.opacity == 0 and self.ids.rent_unpaid.opacity == 0:
            self.ids.show.text = 'Hide Table'
            self.ids.show_total_paid_1.text = "Total:"
            self.ids.show_total_paid_3.text = "For Me:"

            conn = sqlite3.connect('test.db')
            c = conn.cursor()
            c.execute("SELECT *, oid FROM june where oid= 1")
            records = c.fetchall()
            for record in records:
                rent = str(record[0])
                electricity = str(record[1])
                heat = str(record[2])
                water = str(record[3])
                food = str(record[4])
                building = str(record[5])
                internet = str(record[6])
                goofy = str(record[7])
                cigarettes = str(record[8])
                credit = str(record[9])
                additional = str(record[10])

                self.ids.rent_price.text = rent
                self.ids.electricity_price.text = electricity
                self.ids.heat_price.text = heat
                self.ids.water_price.text = water
                self.ids.food_price.text = food
                self.ids.building_price.text = building
                self.ids.internet_price.text = internet
                self.ids.goofy_price.text = goofy
                self.ids.cigarettes_price.text = cigarettes
                self.ids.credit_price.text = credit
                self.ids.additional_price.text = additional
            conn.commit()
            conn.close()

            show_rename_in_table(self)
            self.show_paid_unpaid()
            widgets_enable(self)
        else:
            self.ids.show.text = 'Show Table'
            self.hide()

    def hide(self):
        hide(self)

    def rename(self):
        self.hide()
        rename(self)

    def save_rename(self):
        save_rename(self)
        self.submit_cond()

    def delete(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("DELETE FROM june")
        conn.commit()
        conn.close()

        uncheck(self)
        delete_cond_reset(self)
        self.cancel()
        self.show_total_paid()
        self.submit_cond()
        self.hide()
        self.show()

    def delete_cond(self):
        delete_cond(self)

    def back(self):
        input_numbers(self)
        enable_other(self)
        self.cancel()
        self.hide()
        delete_cond_reset(self)

    def show_paid_unpaid(self):
        show_paid_unpaid(self)

    def add_function(self):
        add_function(self)

    @staticmethod
    def checkbox_state():
        save_checkbox_config()

    def remove_text_on_click(self):
        remove_text_on_click_rename(self)


class July(Screen):
    def submit(self):
        empty_fields_cond(self)
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("INSERT INTO july VALUES (:rent, :electricity, :heat, :water, :food, :building, "
                  ":internet, :goofy, :cigarettes, :credit, :additional)",
                  {'rent': self.ids.rent_input.text[0:4],
                   'electricity': self.ids.electricity_input.text[0:4],
                   'heat': self.ids.heat_input.text[0:4],
                   'water': self.ids.water_input.text[0:4],
                   'food': self.ids.food_input.text[0:4],
                   'building': self.ids.building_input.text[0:4],
                   'internet': self.ids.internet_input.text[0:4],
                   'goofy': self.ids.goofy_input.text[0:4],
                   'cigarettes': self.ids.cigarettes_input.text[0:4],
                   'credit': self.ids.credit_input.text[0:4],
                   'additional': self.ids.additional_input.text[0:4]})
        conn.commit()
        conn.close()

        self.cancel()
        self.show_total_paid()
        self.submit_cond()
        self.hide()
        self.show()

    def submit_cond(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM july where oid= 1")
        records = c.fetchall()
        for record in records:
            self.ids.rent_input.text = str(record[0])
            self.ids.electricity_input.text = str(record[1])
            self.ids.heat_input.text = str(record[2])
            self.ids.water_input.text = str(record[3])
            self.ids.food_input.text = str(record[4])
            self.ids.building_input.text = str(record[5])
            self.ids.internet_input.text = str(record[6])
            self.ids.goofy_input.text = str(record[7])
            self.ids.cigarettes_input.text = str(record[8])
            self.ids.credit_input.text = str(record[9])
            self.ids.additional_input.text = str(record[10])

        if self.ids.rent_input.text == "" and self.ids.electricity_input.text == "" and \
                self.ids.heat_input.text == "" and self.ids.water_input.text == "" and \
                self.ids.food_input.text == "" and self.ids.building_input.text == "" and \
                self.ids.internet_input.text == "" and self.ids.goofy_input.text == "" and \
                self.ids.cigarettes_input.text == "" and self.ids.credit_input.text == "" and \
                self.ids.additional_input.text == "":
            self.ids.submit.disabled = False
        else:
            self.ids.submit.disabled = True

        self.cancel()

        conn.commit()
        conn.close()

    def cancel(self):
        cancel(self)
        self.hide()

    def edit(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT * FROM july WHERE oid = 1")
        records = c.fetchall()
        for record in records:
            rent = str(record[0])
            self.ids.rent_input.text = rent
            electricity = str(record[1])
            self.ids.electricity_input.text = electricity
            heat = str(record[2])
            self.ids.heat_input.text = heat
            water = str(record[3])
            self.ids.water_input.text = water
            food = str(record[4])
            self.ids.food_input.text = food
            building = str(record[5])
            self.ids.building_input.text = building
            internet = str(record[6])
            self.ids.internet_input.text = internet
            goofy = str(record[7])
            self.ids.goofy_input.text = goofy
            cigarettes = str(record[8])
            self.ids.cigarettes_input.text = cigarettes
            credit = str(record[9])
            self.ids.credit_input.text = credit
            additional = str(record[10])
            self.ids.additional_input.text = additional
        conn.commit()
        conn.close()

        add_widgets_enable(self)

    def save(self):
        empty_fields_cond(self)
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("""UPDATE july SET
                                rent = :rent,
                                electricity = :electricity,
                                heat = :heat,
                                water = :water,
                                food = :food,
                                building = :building,
                                internet = :internet,
                                goofy = :goofy,
                                cigarettes = :cigarettes,
                                credit = :credit,
                                additional = :additional

                                WHERE oid = 1""", {
                   'rent': self.ids.rent_input.text[0:4],
                   'electricity': self.ids.electricity_input.text[0:4],
                   'heat': self.ids.heat_input.text[0:4],
                   'water': self.ids.water_input.text[0:4],
                   'food': self.ids.food_input.text[0:4],
                   'building': self.ids.building_input.text[0:4],
                   'internet': self.ids.internet_input.text[0:4],
                   'goofy': self.ids.goofy_input.text[0:4],
                   'cigarettes': self.ids.cigarettes_input.text[0:4],
                   'credit': self.ids.credit_input.text[0:4],
                   'additional': self.ids.additional_input.text[0:4]})
        conn.commit()
        conn.close()

        self.cancel()
        self.hide()
        self.show()
        self.show_total_paid()

    def show_total_paid(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM july where oid= 1")
        records = c.fetchall()
        for record in records:
            a = int(record[0])
            b = int(record[1])
            c = int(record[2])
            d = int(record[3])
            e = int(record[4])
            f = int(record[5])
            g = int(record[6])
            h = int(record[7])
            i = int(record[8])
            j = int(record[9])
            k = int(record[10])

            total = a + b + c + d + e + f + g + h + i + j + k
            me = a / 2 + b / 2 + c / 2 + d / 2 + e / 2 + f / 2 + g / 2 + h / 2 + i + j + k

            if int(self.ids.rent_check.active) == 0:
                total = total - a
                me = round(me - a / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.electricity_check.active) == 0:
                total = total - b
                me = round(me - b / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.heat_check.active) == 0:
                total = total - c
                me = round(me - c / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.water_check.active) == 0:
                total = total - d
                me = round(me - d / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.food_check.active) == 0:
                total = total - e
                me = round(me - e / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.building_check.active) == 0:
                total = total - f
                me = round(me - f / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.internet_check.active) == 0:
                total = total - g
                me = round(me - g / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.goofy_check.active) == 0:
                total = total - h
                me = round(me - h / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.cigarettes_check.active) == 0:
                total = total - i
                me = round(me - i)
            else:
                total = total
                me = round(me)
            if int(self.ids.credit_check.active) == 0:
                total = total - j
                me = round(me - j)
            else:
                total = total
                me = round(me)
            if int(self.ids.additional_check.active) == 0:
                total = total - k
                me = round(me - k)
            else:
                total = total
                me = round(me)

            self.ids.show_total_paid_1.text = "Total:"
            self.ids.show_total_paid_2.text = str(total)
            self.ids.show_total_paid_3.text = "For Me:"
            self.ids.show_total_paid_4.text = str(me)

        conn.commit()
        conn.close()

    def show(self):
        if self.ids.rent_paid.opacity == 0 and self.ids.rent_unpaid.opacity == 0:
            self.ids.show.text = 'Hide Table'
            self.ids.show_total_paid_1.text = "Total:"
            self.ids.show_total_paid_3.text = "For Me:"

            conn = sqlite3.connect('test.db')
            c = conn.cursor()
            c.execute("SELECT *, oid FROM july where oid= 1")
            records = c.fetchall()
            for record in records:
                rent = str(record[0])
                electricity = str(record[1])
                heat = str(record[2])
                water = str(record[3])
                food = str(record[4])
                building = str(record[5])
                internet = str(record[6])
                goofy = str(record[7])
                cigarettes = str(record[8])
                credit = str(record[9])
                additional = str(record[10])

                self.ids.rent_price.text = rent
                self.ids.electricity_price.text = electricity
                self.ids.heat_price.text = heat
                self.ids.water_price.text = water
                self.ids.food_price.text = food
                self.ids.building_price.text = building
                self.ids.internet_price.text = internet
                self.ids.goofy_price.text = goofy
                self.ids.cigarettes_price.text = cigarettes
                self.ids.credit_price.text = credit
                self.ids.additional_price.text = additional
            conn.commit()
            conn.close()

            show_rename_in_table(self)
            self.show_paid_unpaid()
            widgets_enable(self)
        else:
            self.ids.show.text = 'Show Table'
            self.hide()

    def hide(self):
        hide(self)

    def rename(self):
        self.hide()
        rename(self)

    def save_rename(self):
        save_rename(self)
        self.submit_cond()

    def delete(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("DELETE FROM july")
        conn.commit()
        conn.close()

        uncheck(self)
        delete_cond_reset(self)
        self.cancel()
        self.show_total_paid()
        self.submit_cond()
        self.hide()
        self.show()

    def delete_cond(self):
        delete_cond(self)

    def back(self):
        input_numbers(self)
        enable_other(self)
        self.cancel()
        self.hide()
        delete_cond_reset(self)

    def show_paid_unpaid(self):
        show_paid_unpaid(self)

    def add_function(self):
        add_function(self)

    @staticmethod
    def checkbox_state():
        save_checkbox_config()

    def remove_text_on_click(self):
        remove_text_on_click_rename(self)


class August(Screen):
    def submit(self):
        empty_fields_cond(self)
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("INSERT INTO august VALUES (:rent, :electricity, :heat, :water, :food, :building, "
                  ":internet, :goofy, :cigarettes, :credit, :additional)",
                  {'rent': self.ids.rent_input.text[0:4],
                   'electricity': self.ids.electricity_input.text[0:4],
                   'heat': self.ids.heat_input.text[0:4],
                   'water': self.ids.water_input.text[0:4],
                   'food': self.ids.food_input.text[0:4],
                   'building': self.ids.building_input.text[0:4],
                   'internet': self.ids.internet_input.text[0:4],
                   'goofy': self.ids.goofy_input.text[0:4],
                   'cigarettes': self.ids.cigarettes_input.text[0:4],
                   'credit': self.ids.credit_input.text[0:4],
                   'additional': self.ids.additional_input.text[0:4]})
        conn.commit()
        conn.close()

        self.cancel()
        self.show_total_paid()
        self.submit_cond()
        self.hide()
        self.show()

    def submit_cond(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM august where oid= 1")
        records = c.fetchall()
        for record in records:
            self.ids.rent_input.text = str(record[0])
            self.ids.electricity_input.text = str(record[1])
            self.ids.heat_input.text = str(record[2])
            self.ids.water_input.text = str(record[3])
            self.ids.food_input.text = str(record[4])
            self.ids.building_input.text = str(record[5])
            self.ids.internet_input.text = str(record[6])
            self.ids.goofy_input.text = str(record[7])
            self.ids.cigarettes_input.text = str(record[8])
            self.ids.credit_input.text = str(record[9])
            self.ids.additional_input.text = str(record[10])

        if self.ids.rent_input.text == "" and self.ids.electricity_input.text == "" and \
                self.ids.heat_input.text == "" and self.ids.water_input.text == "" and \
                self.ids.food_input.text == "" and self.ids.building_input.text == "" and \
                self.ids.internet_input.text == "" and self.ids.goofy_input.text == "" and \
                self.ids.cigarettes_input.text == "" and self.ids.credit_input.text == "" and \
                self.ids.additional_input.text == "":
            self.ids.submit.disabled = False
        else:
            self.ids.submit.disabled = True

        self.cancel()

        conn.commit()
        conn.close()

    def cancel(self):
        cancel(self)
        self.hide()

    def edit(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT * FROM august WHERE oid = 1")
        records = c.fetchall()
        for record in records:
            rent = str(record[0])
            self.ids.rent_input.text = rent
            electricity = str(record[1])
            self.ids.electricity_input.text = electricity
            heat = str(record[2])
            self.ids.heat_input.text = heat
            water = str(record[3])
            self.ids.water_input.text = water
            food = str(record[4])
            self.ids.food_input.text = food
            building = str(record[5])
            self.ids.building_input.text = building
            internet = str(record[6])
            self.ids.internet_input.text = internet
            goofy = str(record[7])
            self.ids.goofy_input.text = goofy
            cigarettes = str(record[8])
            self.ids.cigarettes_input.text = cigarettes
            credit = str(record[9])
            self.ids.credit_input.text = credit
            additional = str(record[10])
            self.ids.additional_input.text = additional
        conn.commit()
        conn.close()

        add_widgets_enable(self)

    def save(self):
        empty_fields_cond(self)
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("""UPDATE august SET
                                rent = :rent,
                                electricity = :electricity,
                                heat = :heat,
                                water = :water,
                                food = :food,
                                building = :building,
                                internet = :internet,
                                goofy = :goofy,
                                cigarettes = :cigarettes,
                                credit = :credit,
                                additional = :additional

                                WHERE oid = 1""", {
                   'rent': self.ids.rent_input.text[0:4],
                   'electricity': self.ids.electricity_input.text[0:4],
                   'heat': self.ids.heat_input.text[0:4],
                   'water': self.ids.water_input.text[0:4],
                   'food': self.ids.food_input.text[0:4],
                   'building': self.ids.building_input.text[0:4],
                   'internet': self.ids.internet_input.text[0:4],
                   'goofy': self.ids.goofy_input.text[0:4],
                   'cigarettes': self.ids.cigarettes_input.text[0:4],
                   'credit': self.ids.credit_input.text[0:4],
                   'additional': self.ids.additional_input.text[0:4]})
        conn.commit()
        conn.close()

        self.cancel()
        self.hide()
        self.show()
        self.show_total_paid()

    def show_total_paid(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM august where oid= 1")
        records = c.fetchall()
        for record in records:
            a = int(record[0])
            b = int(record[1])
            c = int(record[2])
            d = int(record[3])
            e = int(record[4])
            f = int(record[5])
            g = int(record[6])
            h = int(record[7])
            i = int(record[8])
            j = int(record[9])
            k = int(record[10])

            total = a + b + c + d + e + f + g + h + i + j + k
            me = a / 2 + b / 2 + c / 2 + d / 2 + e / 2 + f / 2 + g / 2 + h / 2 + i + j + k

            if int(self.ids.rent_check.active) == 0:
                total = total - a
                me = round(me - a / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.electricity_check.active) == 0:
                total = total - b
                me = round(me - b / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.heat_check.active) == 0:
                total = total - c
                me = round(me - c / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.water_check.active) == 0:
                total = total - d
                me = round(me - d / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.food_check.active) == 0:
                total = total - e
                me = round(me - e / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.building_check.active) == 0:
                total = total - f
                me = round(me - f / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.internet_check.active) == 0:
                total = total - g
                me = round(me - g / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.goofy_check.active) == 0:
                total = total - h
                me = round(me - h / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.cigarettes_check.active) == 0:
                total = total - i
                me = round(me - i)
            else:
                total = total
                me = round(me)
            if int(self.ids.credit_check.active) == 0:
                total = total - j
                me = round(me - j)
            else:
                total = total
                me = round(me)
            if int(self.ids.additional_check.active) == 0:
                total = total - k
                me = round(me - k)
            else:
                total = total
                me = round(me)

            self.ids.show_total_paid_1.text = "Total:"
            self.ids.show_total_paid_2.text = str(total)
            self.ids.show_total_paid_3.text = "For Me:"
            self.ids.show_total_paid_4.text = str(me)

        conn.commit()
        conn.close()

    def show(self):
        if self.ids.rent_paid.opacity == 0 and self.ids.rent_unpaid.opacity == 0:
            self.ids.show.text = 'Hide Table'
            self.ids.show_total_paid_1.text = "Total:"
            self.ids.show_total_paid_3.text = "For Me:"

            conn = sqlite3.connect('test.db')
            c = conn.cursor()
            c.execute("SELECT *, oid FROM august where oid= 1")
            records = c.fetchall()
            for record in records:
                rent = str(record[0])
                electricity = str(record[1])
                heat = str(record[2])
                water = str(record[3])
                food = str(record[4])
                building = str(record[5])
                internet = str(record[6])
                goofy = str(record[7])
                cigarettes = str(record[8])
                credit = str(record[9])
                additional = str(record[10])

                self.ids.rent_price.text = rent
                self.ids.electricity_price.text = electricity
                self.ids.heat_price.text = heat
                self.ids.water_price.text = water
                self.ids.food_price.text = food
                self.ids.building_price.text = building
                self.ids.internet_price.text = internet
                self.ids.goofy_price.text = goofy
                self.ids.cigarettes_price.text = cigarettes
                self.ids.credit_price.text = credit
                self.ids.additional_price.text = additional
            conn.commit()
            conn.close()

            show_rename_in_table(self)
            self.show_paid_unpaid()
            widgets_enable(self)
        else:
            self.ids.show.text = 'Show Table'
            self.hide()

    def hide(self):
        hide(self)

    def rename(self):
        self.hide()
        rename(self)

    def save_rename(self):
        save_rename(self)
        self.submit_cond()

    def delete(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("DELETE FROM august")
        conn.commit()
        conn.close()

        uncheck(self)
        delete_cond_reset(self)
        self.cancel()
        self.show_total_paid()
        self.submit_cond()
        self.hide()
        self.show()

    def delete_cond(self):
        delete_cond(self)

    def back(self):
        input_numbers(self)
        enable_other(self)
        self.cancel()
        self.hide()
        delete_cond_reset(self)

    def show_paid_unpaid(self):
        show_paid_unpaid(self)

    def add_function(self):
        add_function(self)

    @staticmethod
    def checkbox_state():
        save_checkbox_config()

    def remove_text_on_click(self):
        remove_text_on_click_rename(self)


class September(Screen):
    def submit(self):
        empty_fields_cond(self)
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("INSERT INTO september VALUES (:rent, :electricity, :heat, :water, :food, :building, "
                  ":internet, :goofy, :cigarettes, :credit, :additional)",
                  {'rent': self.ids.rent_input.text[0:4],
                   'electricity': self.ids.electricity_input.text[0:4],
                   'heat': self.ids.heat_input.text[0:4],
                   'water': self.ids.water_input.text[0:4],
                   'food': self.ids.food_input.text[0:4],
                   'building': self.ids.building_input.text[0:4],
                   'internet': self.ids.internet_input.text[0:4],
                   'goofy': self.ids.goofy_input.text[0:4],
                   'cigarettes': self.ids.cigarettes_input.text[0:4],
                   'credit': self.ids.credit_input.text[0:4],
                   'additional': self.ids.additional_input.text[0:4]})
        conn.commit()
        conn.close()

        self.cancel()
        self.show_total_paid()
        self.submit_cond()
        self.hide()
        self.show()

    def submit_cond(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM september where oid= 1")
        records = c.fetchall()
        for record in records:
            self.ids.rent_input.text = str(record[0])
            self.ids.electricity_input.text = str(record[1])
            self.ids.heat_input.text = str(record[2])
            self.ids.water_input.text = str(record[3])
            self.ids.food_input.text = str(record[4])
            self.ids.building_input.text = str(record[5])
            self.ids.internet_input.text = str(record[6])
            self.ids.goofy_input.text = str(record[7])
            self.ids.cigarettes_input.text = str(record[8])
            self.ids.credit_input.text = str(record[9])
            self.ids.additional_input.text = str(record[10])

        if self.ids.rent_input.text == "" and self.ids.electricity_input.text == "" and \
                self.ids.heat_input.text == "" and self.ids.water_input.text == "" and \
                self.ids.food_input.text == "" and self.ids.building_input.text == "" and \
                self.ids.internet_input.text == "" and self.ids.goofy_input.text == "" and \
                self.ids.cigarettes_input.text == "" and self.ids.credit_input.text == "" and \
                self.ids.additional_input.text == "":
            self.ids.submit.disabled = False
        else:
            self.ids.submit.disabled = True

        self.cancel()

        conn.commit()
        conn.close()

    def cancel(self):
        cancel(self)
        self.hide()

    def edit(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT * FROM september WHERE oid = 1")
        records = c.fetchall()
        for record in records:
            rent = str(record[0])
            self.ids.rent_input.text = rent
            electricity = str(record[1])
            self.ids.electricity_input.text = electricity
            heat = str(record[2])
            self.ids.heat_input.text = heat
            water = str(record[3])
            self.ids.water_input.text = water
            food = str(record[4])
            self.ids.food_input.text = food
            building = str(record[5])
            self.ids.building_input.text = building
            internet = str(record[6])
            self.ids.internet_input.text = internet
            goofy = str(record[7])
            self.ids.goofy_input.text = goofy
            cigarettes = str(record[8])
            self.ids.cigarettes_input.text = cigarettes
            credit = str(record[9])
            self.ids.credit_input.text = credit
            additional = str(record[10])
            self.ids.additional_input.text = additional
        conn.commit()
        conn.close()

        add_widgets_enable(self)

    def save(self):
        empty_fields_cond(self)
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("""UPDATE september SET
                                rent = :rent,
                                electricity = :electricity,
                                heat = :heat,
                                water = :water,
                                food = :food,
                                building = :building,
                                internet = :internet,
                                goofy = :goofy,
                                cigarettes = :cigarettes,
                                credit = :credit,
                                additional = :additional

                                WHERE oid = 1""", {
                   'rent': self.ids.rent_input.text[0:4],
                   'electricity': self.ids.electricity_input.text[0:4],
                   'heat': self.ids.heat_input.text[0:4],
                   'water': self.ids.water_input.text[0:4],
                   'food': self.ids.food_input.text[0:4],
                   'building': self.ids.building_input.text[0:4],
                   'internet': self.ids.internet_input.text[0:4],
                   'goofy': self.ids.goofy_input.text[0:4],
                   'cigarettes': self.ids.cigarettes_input.text[0:4],
                   'credit': self.ids.credit_input.text[0:4],
                   'additional': self.ids.additional_input.text[0:4]})
        conn.commit()
        conn.close()

        self.cancel()
        self.hide()
        self.show()
        self.show_total_paid()

    def show_total_paid(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM september where oid= 1")
        records = c.fetchall()
        for record in records:
            a = int(record[0])
            b = int(record[1])
            c = int(record[2])
            d = int(record[3])
            e = int(record[4])
            f = int(record[5])
            g = int(record[6])
            h = int(record[7])
            i = int(record[8])
            j = int(record[9])
            k = int(record[10])

            total = a + b + c + d + e + f + g + h + i + j + k
            me = a / 2 + b / 2 + c / 2 + d / 2 + e / 2 + f / 2 + g / 2 + h / 2 + i + j + k

            if int(self.ids.rent_check.active) == 0:
                total = total - a
                me = round(me - a / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.electricity_check.active) == 0:
                total = total - b
                me = round(me - b / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.heat_check.active) == 0:
                total = total - c
                me = round(me - c / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.water_check.active) == 0:
                total = total - d
                me = round(me - d / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.food_check.active) == 0:
                total = total - e
                me = round(me - e / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.building_check.active) == 0:
                total = total - f
                me = round(me - f / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.internet_check.active) == 0:
                total = total - g
                me = round(me - g / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.goofy_check.active) == 0:
                total = total - h
                me = round(me - h / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.cigarettes_check.active) == 0:
                total = total - i
                me = round(me - i)
            else:
                total = total
                me = round(me)
            if int(self.ids.credit_check.active) == 0:
                total = total - j
                me = round(me - j)
            else:
                total = total
                me = round(me)
            if int(self.ids.additional_check.active) == 0:
                total = total - k
                me = round(me - k)
            else:
                total = total
                me = round(me)

            self.ids.show_total_paid_1.text = "Total:"
            self.ids.show_total_paid_2.text = str(total)
            self.ids.show_total_paid_3.text = "For Me:"
            self.ids.show_total_paid_4.text = str(me)

        conn.commit()
        conn.close()

    def show(self):
        if self.ids.rent_paid.opacity == 0 and self.ids.rent_unpaid.opacity == 0:
            self.ids.show.text = 'Hide Table'
            self.ids.show_total_paid_1.text = "Total:"
            self.ids.show_total_paid_3.text = "For Me:"

            conn = sqlite3.connect('test.db')
            c = conn.cursor()
            c.execute("SELECT *, oid FROM september where oid= 1")
            records = c.fetchall()
            for record in records:
                rent = str(record[0])
                electricity = str(record[1])
                heat = str(record[2])
                water = str(record[3])
                food = str(record[4])
                building = str(record[5])
                internet = str(record[6])
                goofy = str(record[7])
                cigarettes = str(record[8])
                credit = str(record[9])
                additional = str(record[10])

                self.ids.rent_price.text = rent
                self.ids.electricity_price.text = electricity
                self.ids.heat_price.text = heat
                self.ids.water_price.text = water
                self.ids.food_price.text = food
                self.ids.building_price.text = building
                self.ids.internet_price.text = internet
                self.ids.goofy_price.text = goofy
                self.ids.cigarettes_price.text = cigarettes
                self.ids.credit_price.text = credit
                self.ids.additional_price.text = additional
            conn.commit()
            conn.close()

            show_rename_in_table(self)
            self.show_paid_unpaid()
            widgets_enable(self)
        else:
            self.ids.show.text = 'Show Table'
            self.hide()

    def hide(self):
        hide(self)

    def rename(self):
        self.hide()
        rename(self)

    def save_rename(self):
        save_rename(self)
        self.submit_cond()

    def delete(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("DELETE FROM september")
        conn.commit()
        conn.close()

        uncheck(self)
        delete_cond_reset(self)
        self.cancel()
        self.show_total_paid()
        self.submit_cond()
        self.hide()
        self.show()

    def delete_cond(self):
        delete_cond(self)

    def back(self):
        input_numbers(self)
        enable_other(self)
        self.cancel()
        self.hide()
        delete_cond_reset(self)

    def show_paid_unpaid(self):
        show_paid_unpaid(self)

    def add_function(self):
        add_function(self)

    @staticmethod
    def checkbox_state():
        save_checkbox_config()

    def remove_text_on_click(self):
        remove_text_on_click_rename(self)


class October(Screen):
    def submit(self):
        empty_fields_cond(self)
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("INSERT INTO october VALUES (:rent, :electricity, :heat, :water, :food, :building, "
                  ":internet, :goofy, :cigarettes, :credit, :additional)",
                  {'rent': self.ids.rent_input.text[0:4],
                   'electricity': self.ids.electricity_input.text[0:4],
                   'heat': self.ids.heat_input.text[0:4],
                   'water': self.ids.water_input.text[0:4],
                   'food': self.ids.food_input.text[0:4],
                   'building': self.ids.building_input.text[0:4],
                   'internet': self.ids.internet_input.text[0:4],
                   'goofy': self.ids.goofy_input.text[0:4],
                   'cigarettes': self.ids.cigarettes_input.text[0:4],
                   'credit': self.ids.credit_input.text[0:4],
                   'additional': self.ids.additional_input.text[0:4]})
        conn.commit()
        conn.close()

        self.cancel()
        self.show_total_paid()
        self.submit_cond()
        self.hide()
        self.show()

    def submit_cond(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM october where oid= 1")
        records = c.fetchall()
        for record in records:
            self.ids.rent_input.text = str(record[0])
            self.ids.electricity_input.text = str(record[1])
            self.ids.heat_input.text = str(record[2])
            self.ids.water_input.text = str(record[3])
            self.ids.food_input.text = str(record[4])
            self.ids.building_input.text = str(record[5])
            self.ids.internet_input.text = str(record[6])
            self.ids.goofy_input.text = str(record[7])
            self.ids.cigarettes_input.text = str(record[8])
            self.ids.credit_input.text = str(record[9])
            self.ids.additional_input.text = str(record[10])

        if self.ids.rent_input.text == "" and self.ids.electricity_input.text == "" and \
                self.ids.heat_input.text == "" and self.ids.water_input.text == "" and \
                self.ids.food_input.text == "" and self.ids.building_input.text == "" and \
                self.ids.internet_input.text == "" and self.ids.goofy_input.text == "" and \
                self.ids.cigarettes_input.text == "" and self.ids.credit_input.text == "" and \
                self.ids.additional_input.text == "":
            self.ids.submit.disabled = False
        else:
            self.ids.submit.disabled = True

        self.cancel()

        conn.commit()
        conn.close()

    def cancel(self):
        cancel(self)
        self.hide()

    def edit(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT * FROM october WHERE oid = 1")
        records = c.fetchall()
        for record in records:
            rent = str(record[0])
            self.ids.rent_input.text = rent
            electricity = str(record[1])
            self.ids.electricity_input.text = electricity
            heat = str(record[2])
            self.ids.heat_input.text = heat
            water = str(record[3])
            self.ids.water_input.text = water
            food = str(record[4])
            self.ids.food_input.text = food
            building = str(record[5])
            self.ids.building_input.text = building
            internet = str(record[6])
            self.ids.internet_input.text = internet
            goofy = str(record[7])
            self.ids.goofy_input.text = goofy
            cigarettes = str(record[8])
            self.ids.cigarettes_input.text = cigarettes
            credit = str(record[9])
            self.ids.credit_input.text = credit
            additional = str(record[10])
            self.ids.additional_input.text = additional
        conn.commit()
        conn.close()

        add_widgets_enable(self)

    def save(self):
        empty_fields_cond(self)
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("""UPDATE october SET
                                rent = :rent,
                                electricity = :electricity,
                                heat = :heat,
                                water = :water,
                                food = :food,
                                building = :building,
                                internet = :internet,
                                goofy = :goofy,
                                cigarettes = :cigarettes,
                                credit = :credit,
                                additional = :additional

                                WHERE oid = 1""", {
                   'rent': self.ids.rent_input.text[0:4],
                   'electricity': self.ids.electricity_input.text[0:4],
                   'heat': self.ids.heat_input.text[0:4],
                   'water': self.ids.water_input.text[0:4],
                   'food': self.ids.food_input.text[0:4],
                   'building': self.ids.building_input.text[0:4],
                   'internet': self.ids.internet_input.text[0:4],
                   'goofy': self.ids.goofy_input.text[0:4],
                   'cigarettes': self.ids.cigarettes_input.text[0:4],
                   'credit': self.ids.credit_input.text[0:4],
                   'additional': self.ids.additional_input.text[0:4]})
        conn.commit()
        conn.close()

        self.cancel()
        self.hide()
        self.show()
        self.show_total_paid()

    def show_total_paid(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM october where oid= 1")
        records = c.fetchall()
        for record in records:
            a = int(record[0])
            b = int(record[1])
            c = int(record[2])
            d = int(record[3])
            e = int(record[4])
            f = int(record[5])
            g = int(record[6])
            h = int(record[7])
            i = int(record[8])
            j = int(record[9])
            k = int(record[10])

            total = a + b + c + d + e + f + g + h + i + j + k
            me = a / 2 + b / 2 + c / 2 + d / 2 + e / 2 + f / 2 + g / 2 + h / 2 + i + j + k

            if int(self.ids.rent_check.active) == 0:
                total = total - a
                me = round(me - a / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.electricity_check.active) == 0:
                total = total - b
                me = round(me - b / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.heat_check.active) == 0:
                total = total - c
                me = round(me - c / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.water_check.active) == 0:
                total = total - d
                me = round(me - d / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.food_check.active) == 0:
                total = total - e
                me = round(me - e / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.building_check.active) == 0:
                total = total - f
                me = round(me - f / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.internet_check.active) == 0:
                total = total - g
                me = round(me - g / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.goofy_check.active) == 0:
                total = total - h
                me = round(me - h / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.cigarettes_check.active) == 0:
                total = total - i
                me = round(me - i)
            else:
                total = total
                me = round(me)
            if int(self.ids.credit_check.active) == 0:
                total = total - j
                me = round(me - j)
            else:
                total = total
                me = round(me)
            if int(self.ids.additional_check.active) == 0:
                total = total - k
                me = round(me - k)
            else:
                total = total
                me = round(me)

            self.ids.show_total_paid_1.text = "Total:"
            self.ids.show_total_paid_2.text = str(total)
            self.ids.show_total_paid_3.text = "For Me:"
            self.ids.show_total_paid_4.text = str(me)

        conn.commit()
        conn.close()

    def show(self):
        if self.ids.rent_paid.opacity == 0 and self.ids.rent_unpaid.opacity == 0:
            self.ids.show.text = 'Hide Table'
            self.ids.show_total_paid_1.text = "Total:"
            self.ids.show_total_paid_3.text = "For Me:"

            conn = sqlite3.connect('test.db')
            c = conn.cursor()
            c.execute("SELECT *, oid FROM october where oid= 1")
            records = c.fetchall()
            for record in records:
                rent = str(record[0])
                electricity = str(record[1])
                heat = str(record[2])
                water = str(record[3])
                food = str(record[4])
                building = str(record[5])
                internet = str(record[6])
                goofy = str(record[7])
                cigarettes = str(record[8])
                credit = str(record[9])
                additional = str(record[10])

                self.ids.rent_price.text = rent
                self.ids.electricity_price.text = electricity
                self.ids.heat_price.text = heat
                self.ids.water_price.text = water
                self.ids.food_price.text = food
                self.ids.building_price.text = building
                self.ids.internet_price.text = internet
                self.ids.goofy_price.text = goofy
                self.ids.cigarettes_price.text = cigarettes
                self.ids.credit_price.text = credit
                self.ids.additional_price.text = additional
            conn.commit()
            conn.close()

            show_rename_in_table(self)
            self.show_paid_unpaid()
            widgets_enable(self)
        else:
            self.ids.show.text = 'Show Table'
            self.hide()

    def hide(self):
        hide(self)

    def rename(self):
        self.hide()
        rename(self)

    def save_rename(self):
        save_rename(self)
        self.submit_cond()

    def delete(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("DELETE FROM october")
        conn.commit()
        conn.close()

        uncheck(self)
        delete_cond_reset(self)
        self.cancel()
        self.show_total_paid()
        self.submit_cond()
        self.hide()
        self.show()

    def delete_cond(self):
        delete_cond(self)

    def back(self):
        input_numbers(self)
        enable_other(self)
        self.cancel()
        self.hide()
        delete_cond_reset(self)

    def show_paid_unpaid(self):
        show_paid_unpaid(self)

    def add_function(self):
        add_function(self)

    @staticmethod
    def checkbox_state():
        save_checkbox_config()

    def remove_text_on_click(self):
        remove_text_on_click_rename(self)


class November(Screen):
    def submit(self):
        empty_fields_cond(self)
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("INSERT INTO november VALUES (:rent, :electricity, :heat, :water, :food, :building, "
                  ":internet, :goofy, :cigarettes, :credit, :additional)",
                  {'rent': self.ids.rent_input.text[0:4],
                   'electricity': self.ids.electricity_input.text[0:4],
                   'heat': self.ids.heat_input.text[0:4],
                   'water': self.ids.water_input.text[0:4],
                   'food': self.ids.food_input.text[0:4],
                   'building': self.ids.building_input.text[0:4],
                   'internet': self.ids.internet_input.text[0:4],
                   'goofy': self.ids.goofy_input.text[0:4],
                   'cigarettes': self.ids.cigarettes_input.text[0:4],
                   'credit': self.ids.credit_input.text[0:4],
                   'additional': self.ids.additional_input.text[0:4]})
        conn.commit()
        conn.close()

        self.cancel()
        self.show_total_paid()
        self.submit_cond()
        self.hide()
        self.show()

    def submit_cond(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM november where oid= 1")
        records = c.fetchall()
        for record in records:
            self.ids.rent_input.text = str(record[0])
            self.ids.electricity_input.text = str(record[1])
            self.ids.heat_input.text = str(record[2])
            self.ids.water_input.text = str(record[3])
            self.ids.food_input.text = str(record[4])
            self.ids.building_input.text = str(record[5])
            self.ids.internet_input.text = str(record[6])
            self.ids.goofy_input.text = str(record[7])
            self.ids.cigarettes_input.text = str(record[8])
            self.ids.credit_input.text = str(record[9])
            self.ids.additional_input.text = str(record[10])

        if self.ids.rent_input.text == "" and self.ids.electricity_input.text == "" and \
                self.ids.heat_input.text == "" and self.ids.water_input.text == "" and \
                self.ids.food_input.text == "" and self.ids.building_input.text == "" and \
                self.ids.internet_input.text == "" and self.ids.goofy_input.text == "" and \
                self.ids.cigarettes_input.text == "" and self.ids.credit_input.text == "" and \
                self.ids.additional_input.text == "":
            self.ids.submit.disabled = False
        else:
            self.ids.submit.disabled = True

        self.cancel()

        conn.commit()
        conn.close()

    def cancel(self):
        cancel(self)
        self.hide()

    def edit(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT * FROM november WHERE oid = 1")
        records = c.fetchall()
        for record in records:
            rent = str(record[0])
            self.ids.rent_input.text = rent
            electricity = str(record[1])
            self.ids.electricity_input.text = electricity
            heat = str(record[2])
            self.ids.heat_input.text = heat
            water = str(record[3])
            self.ids.water_input.text = water
            food = str(record[4])
            self.ids.food_input.text = food
            building = str(record[5])
            self.ids.building_input.text = building
            internet = str(record[6])
            self.ids.internet_input.text = internet
            goofy = str(record[7])
            self.ids.goofy_input.text = goofy
            cigarettes = str(record[8])
            self.ids.cigarettes_input.text = cigarettes
            cigarettes = str(record[9])
            self.ids.credit_input.text = cigarettes
            additional = str(record[10])
            self.ids.additional_input.text = additional
        conn.commit()
        conn.close()

        add_widgets_enable(self)

    def save(self):
        empty_fields_cond(self)
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("""UPDATE november SET
                                rent = :rent,
                                electricity = :electricity,
                                heat = :heat,
                                water = :water,
                                food = :food,
                                building = :building,
                                internet = :internet,
                                goofy = :goofy,
                                cigarettes = :cigarettes,
                                credit = :credit,
                                additional = :additional

                                WHERE oid = 1""", {
                   'rent': self.ids.rent_input.text[0:4],
                   'electricity': self.ids.electricity_input.text[0:4],
                   'heat': self.ids.heat_input.text[0:4],
                   'water': self.ids.water_input.text[0:4],
                   'food': self.ids.food_input.text[0:4],
                   'building': self.ids.building_input.text[0:4],
                   'internet': self.ids.internet_input.text[0:4],
                   'goofy': self.ids.goofy_input.text[0:4],
                   'cigarettes': self.ids.cigarettes_input.text[0:4],
                   'credit': self.ids.credit_input.text[0:4],
                   'additional': self.ids.additional_input.text[0:4]})
        conn.commit()
        conn.close()

        self.cancel()
        self.hide()
        self.show()
        self.show_total_paid()

    def show_total_paid(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM november where oid= 1")
        records = c.fetchall()
        for record in records:
            a = int(record[0])
            b = int(record[1])
            c = int(record[2])
            d = int(record[3])
            e = int(record[4])
            f = int(record[5])
            g = int(record[6])
            h = int(record[7])
            i = int(record[8])
            j = int(record[9])
            k = int(record[10])

            total = a + b + c + d + e + f + g + h + i + j + k
            me = a / 2 + b / 2 + c / 2 + d / 2 + e / 2 + f / 2 + g / 2 + h / 2 + i + j + k

            if int(self.ids.rent_check.active) == 0:
                total = total - a
                me = round(me - a / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.electricity_check.active) == 0:
                total = total - b
                me = round(me - b / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.heat_check.active) == 0:
                total = total - c
                me = round(me - c / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.water_check.active) == 0:
                total = total - d
                me = round(me - d / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.food_check.active) == 0:
                total = total - e
                me = round(me - e / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.building_check.active) == 0:
                total = total - f
                me = round(me - f / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.internet_check.active) == 0:
                total = total - g
                me = round(me - g / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.goofy_check.active) == 0:
                total = total - h
                me = round(me - h / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.cigarettes_check.active) == 0:
                total = total - i
                me = round(me - i)
            else:
                total = total
                me = round(me)
            if int(self.ids.credit_check.active) == 0:
                total = total - j
                me = round(me - j)
            else:
                total = total
                me = round(me)
            if int(self.ids.additional_check.active) == 0:
                total = total - k
                me = round(me - k)
            else:
                total = total
                me = round(me)

            self.ids.show_total_paid_1.text = "Total:"
            self.ids.show_total_paid_2.text = str(total)
            self.ids.show_total_paid_3.text = "For Me:"
            self.ids.show_total_paid_4.text = str(me)

        conn.commit()
        conn.close()

    def show(self):
        if self.ids.rent_paid.opacity == 0 and self.ids.rent_unpaid.opacity == 0:
            self.ids.show.text = 'Hide Table'
            self.ids.show_total_paid_1.text = "Total:"
            self.ids.show_total_paid_3.text = "For Me:"

            conn = sqlite3.connect('test.db')
            c = conn.cursor()
            c.execute("SELECT *, oid FROM november where oid= 1")
            records = c.fetchall()
            for record in records:
                rent = str(record[0])
                electricity = str(record[1])
                heat = str(record[2])
                water = str(record[3])
                food = str(record[4])
                building = str(record[5])
                internet = str(record[6])
                goofy = str(record[7])
                cigarettes = str(record[8])
                credit = str(record[9])
                additional = str(record[10])

                self.ids.rent_price.text = rent
                self.ids.electricity_price.text = electricity
                self.ids.heat_price.text = heat
                self.ids.water_price.text = water
                self.ids.food_price.text = food
                self.ids.building_price.text = building
                self.ids.internet_price.text = internet
                self.ids.goofy_price.text = goofy
                self.ids.cigarettes_price.text = cigarettes
                self.ids.credit_price.text = credit
                self.ids.additional_price.text = additional
            conn.commit()
            conn.close()

            show_rename_in_table(self)
            self.show_paid_unpaid()
            widgets_enable(self)
        else:
            self.ids.show.text = 'Show Table'
            self.hide()

    def hide(self):
        hide(self)

    def rename(self):
        self.hide()
        rename(self)

    def save_rename(self):
        save_rename(self)
        self.submit_cond()

    def delete(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("DELETE FROM november")
        conn.commit()
        conn.close()

        uncheck(self)
        delete_cond_reset(self)
        self.cancel()
        self.show_total_paid()
        self.submit_cond()
        self.hide()
        self.show()

    def delete_cond(self):
        delete_cond(self)

    def back(self):
        input_numbers(self)
        enable_other(self)
        self.cancel()
        self.hide()
        delete_cond_reset(self)

    def show_paid_unpaid(self):
        show_paid_unpaid(self)

    def add_function(self):
        add_function(self)

    @staticmethod
    def checkbox_state():
        save_checkbox_config()

    def remove_text_on_click(self):
        remove_text_on_click_rename(self)


class December(Screen):
    def submit(self):
        empty_fields_cond(self)
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("INSERT INTO december VALUES (:rent, :electricity, :heat, :water, :food, :building, "
                  ":internet, :goofy, :cigarettes, :credit, :additional)",
                  {'rent': self.ids.rent_input.text[0:4],
                   'electricity': self.ids.electricity_input.text[0:4],
                   'heat': self.ids.heat_input.text[0:4],
                   'water': self.ids.water_input.text[0:4],
                   'food': self.ids.food_input.text[0:4],
                   'building': self.ids.building_input.text[0:4],
                   'internet': self.ids.internet_input.text[0:4],
                   'goofy': self.ids.goofy_input.text[0:4],
                   'cigarettes': self.ids.cigarettes_input.text[0:4],
                   'credit': self.ids.credit_input.text[0:4],
                   'additional': self.ids.additional_input.text[0:4]})
        conn.commit()
        conn.close()

        self.cancel()
        self.show_total_paid()
        self.submit_cond()
        self.hide()
        self.show()

    def submit_cond(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM december where oid= 1")
        records = c.fetchall()
        for record in records:
            self.ids.rent_input.text = str(record[0])
            self.ids.electricity_input.text = str(record[1])
            self.ids.heat_input.text = str(record[2])
            self.ids.water_input.text = str(record[3])
            self.ids.food_input.text = str(record[4])
            self.ids.building_input.text = str(record[5])
            self.ids.internet_input.text = str(record[6])
            self.ids.goofy_input.text = str(record[7])
            self.ids.cigarettes_input.text = str(record[8])
            self.ids.credit_input.text = str(record[9])
            self.ids.additional_input.text = str(record[10])

        if self.ids.rent_input.text == "" and self.ids.electricity_input.text == "" and \
                self.ids.heat_input.text == "" and self.ids.water_input.text == "" and \
                self.ids.food_input.text == "" and self.ids.building_input.text == "" and \
                self.ids.internet_input.text == "" and self.ids.goofy_input.text == "" and \
                self.ids.cigarettes_input.text == "" and self.ids.credit_input.text == "" and \
                self.ids.additional_input.text == "":
            self.ids.submit.disabled = False
        else:
            self.ids.submit.disabled = True

        self.cancel()

        conn.commit()
        conn.close()

    def cancel(self):
        cancel(self)
        self.hide()

    def edit(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT * FROM december WHERE oid = 1")
        records = c.fetchall()
        for record in records:
            rent = str(record[0])
            self.ids.rent_input.text = rent
            electricity = str(record[1])
            self.ids.electricity_input.text = electricity
            heat = str(record[2])
            self.ids.heat_input.text = heat
            water = str(record[3])
            self.ids.water_input.text = water
            food = str(record[4])
            self.ids.food_input.text = food
            building = str(record[5])
            self.ids.building_input.text = building
            internet = str(record[6])
            self.ids.internet_input.text = internet
            goofy = str(record[7])
            self.ids.goofy_input.text = goofy
            cigarettes = str(record[8])
            self.ids.cigarettes_input.text = cigarettes
            credit = str(record[9])
            self.ids.credit_input.text = credit
            additional = str(record[10])
            self.ids.additional_input.text = additional
        conn.commit()
        conn.close()

        add_widgets_enable(self)

    def save(self):
        empty_fields_cond(self)
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("""UPDATE december SET
                                rent = :rent,
                                electricity = :electricity,
                                heat = :heat,
                                water = :water,
                                food = :food,
                                building = :building,
                                internet = :internet,
                                goofy = :goofy,
                                cigarettes = :cigarettes,
                                credit = :credit,
                                additional = :additional

                                WHERE oid = 1""", {
                   'rent': self.ids.rent_input.text[0:4],
                   'electricity': self.ids.electricity_input.text[0:4],
                   'heat': self.ids.heat_input.text[0:4],
                   'water': self.ids.water_input.text[0:4],
                   'food': self.ids.food_input.text[0:4],
                   'building': self.ids.building_input.text[0:4],
                   'internet': self.ids.internet_input.text[0:4],
                   'goofy': self.ids.goofy_input.text[0:4],
                   'cigarettes': self.ids.cigarettes_input.text[0:4],
                   'credit': self.ids.credit_input.text[0:4],
                   'additional': self.ids.additional_input.text[0:4]})
        conn.commit()
        conn.close()

        self.cancel()
        self.hide()
        self.show()
        self.show_total_paid()

    def show_total_paid(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM december where oid= 1")
        records = c.fetchall()
        for record in records:
            a = int(record[0])
            b = int(record[1])
            c = int(record[2])
            d = int(record[3])
            e = int(record[4])
            f = int(record[5])
            g = int(record[6])
            h = int(record[7])
            i = int(record[8])
            j = int(record[9])
            k = int(record[10])

            total = a + b + c + d + e + f + g + h + i + j + k
            me = a / 2 + b / 2 + c / 2 + d / 2 + e / 2 + f / 2 + g / 2 + h / 2 + i + j + k

            if int(self.ids.rent_check.active) == 0:
                total = total - a
                me = round(me - a / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.electricity_check.active) == 0:
                total = total - b
                me = round(me - b / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.heat_check.active) == 0:
                total = total - c
                me = round(me - c / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.water_check.active) == 0:
                total = total - d
                me = round(me - d / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.food_check.active) == 0:
                total = total - e
                me = round(me - e / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.building_check.active) == 0:
                total = total - f
                me = round(me - f / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.internet_check.active) == 0:
                total = total - g
                me = round(me - g / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.goofy_check.active) == 0:
                total = total - h
                me = round(me - h / 2)
            else:
                total = total
                me = round(me)
            if int(self.ids.cigarettes_check.active) == 0:
                total = total - i
                me = round(me - i)
            else:
                total = total
                me = round(me)
            if int(self.ids.credit_check.active) == 0:
                total = total - j
                me = round(me - j)
            else:
                total = total
                me = round(me)
            if int(self.ids.additional_check.active) == 0:
                total = total - k
                me = round(me - k)
            else:
                total = total
                me = round(me)

            self.ids.show_total_paid_1.text = "Total:"
            self.ids.show_total_paid_2.text = str(total)
            self.ids.show_total_paid_3.text = "For Me:"
            self.ids.show_total_paid_4.text = str(me)

        conn.commit()
        conn.close()

    def show(self):
        if self.ids.rent_paid.opacity == 0 and self.ids.rent_unpaid.opacity == 0:
            self.ids.show.text = 'Hide Table'
            self.ids.show_total_paid_1.text = "Total:"
            self.ids.show_total_paid_3.text = "For Me:"

            conn = sqlite3.connect('test.db')
            c = conn.cursor()
            c.execute("SELECT *, oid FROM december where oid= 1")
            records = c.fetchall()
            for record in records:
                rent = str(record[0])
                electricity = str(record[1])
                heat = str(record[2])
                water = str(record[3])
                food = str(record[4])
                building = str(record[5])
                internet = str(record[6])
                goofy = str(record[7])
                cigarettes = str(record[8])
                credit = str(record[9])
                additional = str(record[10])

                self.ids.rent_price.text = rent
                self.ids.electricity_price.text = electricity
                self.ids.heat_price.text = heat
                self.ids.water_price.text = water
                self.ids.food_price.text = food
                self.ids.building_price.text = building
                self.ids.internet_price.text = internet
                self.ids.goofy_price.text = goofy
                self.ids.cigarettes_price.text = cigarettes
                self.ids.credit_price.text = credit
                self.ids.additional_price.text = additional
            conn.commit()
            conn.close()

            show_rename_in_table(self)
            self.show_paid_unpaid()
            widgets_enable(self)
        else:
            self.ids.show.text = 'Show Table'
            self.hide()

    def hide(self):
        hide(self)

    def rename(self):
        self.hide()
        rename(self)

    def save_rename(self):
        save_rename(self)
        self.submit_cond()

    def delete(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("DELETE FROM december")
        conn.commit()
        conn.close()

        uncheck(self)
        delete_cond_reset(self)
        self.cancel()
        self.show_total_paid()
        self.submit_cond()
        self.hide()
        self.show()

    def delete_cond(self):
        delete_cond(self)

    def back(self):
        input_numbers(self)
        enable_other(self)
        self.cancel()
        self.hide()
        delete_cond_reset(self)

    def show_paid_unpaid(self):
        show_paid_unpaid(self)

    def add_function(self):
        add_function(self)

    @staticmethod
    def checkbox_state():
        save_checkbox_config()

    def remove_text_on_click(self):
        remove_text_on_click_rename(self)


# Building the Report Screen
class Report(Screen):
    def submit(self):
        self.empty_fields_cond()
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("INSERT INTO income VALUES (:january, :february, :march, :april, :may, :june, "
                  ":july, :august, :september, :october, :november, :december)",

                  {'january': self.ids.january_income.text,
                   'february': self.ids.february_income.text,
                   'march': self.ids.march_income.text,
                   'april': self.ids.april_income.text,
                   'may': self.ids.may_income.text,
                   'june': self.ids.june_income.text,
                   'july': self.ids.july_income.text,
                   'august': self.ids.august_income.text,
                   'september': self.ids.september_income.text,
                   'october': self.ids.october_income.text,
                   'november': self.ids.november_income.text,
                   'december': self.ids.december_income.text})

        c.execute("INSERT INTO available VALUES (:january, :february, :march, :april, :may, :june, "
                  ":july, :august, :september, :october, :november, :december)",

                  {'january': self.ids.january_available.text,
                   'february': self.ids.february_available.text,
                   'march': self.ids.march_available.text,
                   'april': self.ids.april_available.text,
                   'may': self.ids.may_available.text,
                   'june': self.ids.june_available.text,
                   'july': self.ids.july_available.text,
                   'august': self.ids.august_available.text,
                   'september': self.ids.september_available.text,
                   'october': self.ids.october_available.text,
                   'november': self.ids.november_available.text,
                   'december': self.ids.december_available.text})
        conn.commit()
        conn.close()

        self.show()
        self.clear()

        screens[2].export_data()
        screens[2].calculate_left()
        screens[2].calculate_others()

    def submit_cond(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM income where oid= 1")
        records = c.fetchall()
        for record in records:
            self.ids.inc_1.text = str(record[0])
            self.ids.inc_2.text = str(record[1])
            self.ids.inc_3.text = str(record[2])
            self.ids.inc_4.text = str(record[3])
            self.ids.inc_5.text = str(record[4])
            self.ids.inc_6.text = str(record[5])
            self.ids.inc_7.text = str(record[6])
            self.ids.inc_8.text = str(record[7])
            self.ids.inc_9.text = str(record[8])
            self.ids.inc_10.text = str(record[9])
            self.ids.inc_11.text = str(record[10])
            self.ids.inc_12.text = str(record[11])

        if self.ids.inc_1.text == "0" and self.ids.inc_2.text == "0" and self.ids.inc_3.text == "0" and \
                self.ids.inc_4.text == "0" and self.ids.inc_5.text == "0" and self.ids.inc_6.text == "0" and \
                self.ids.inc_7.text == "0" and self.ids.inc_8.text == "0" and self.ids.inc_9.text == "0" and \
                self.ids.inc_10.text == "0" and self.ids.inc_11.text == "0" and self.ids.inc_12.text == "0":
            self.ids.submit_report.disabled = False
        else:
            self.ids.submit_report.disabled = True

        conn.commit()
        conn.close()

    def empty_fields_cond(self):
        if self.ids.january_income.text == "":
            self.ids.january_income.text = "0"
        if self.ids.february_income.text == "":
            self.ids.february_income.text = "0"
        if self.ids.march_income.text == "":
            self.ids.march_income.text = "0"
        if self.ids.april_income.text == "":
            self.ids.april_income.text = "0"
        if self.ids.may_income.text == "":
            self.ids.may_income.text = "0"
        if self.ids.june_income.text == "":
            self.ids.june_income.text = "0"
        if self.ids.july_income.text == "":
            self.ids.july_income.text = "0"
        if self.ids.august_income.text == "":
            self.ids.august_income.text = "0"
        if self.ids.september_income.text == "":
            self.ids.september_income.text = "0"
        if self.ids.october_income.text == "":
            self.ids.october_income.text = "0"
        if self.ids.november_income.text == "":
            self.ids.november_income.text = "0"
        if self.ids.december_income.text == "":
            self.ids.december_income.text = "0"

        if self.ids.january_available.text == "":
            self.ids.january_available.text = "0"
        if self.ids.february_available.text == "":
            self.ids.february_available.text = "0"
        if self.ids.march_available.text == "":
            self.ids.march_available.text = "0"
        if self.ids.april_available.text == "":
            self.ids.april_available.text = "0"
        if self.ids.may_available.text == "":
            self.ids.may_available.text = "0"
        if self.ids.june_available.text == "":
            self.ids.june_available.text = "0"
        if self.ids.july_available.text == "":
            self.ids.july_available.text = "0"
        if self.ids.august_available.text == "":
            self.ids.august_available.text = "0"
        if self.ids.september_available.text == "":
            self.ids.september_available.text = "0"
        if self.ids.october_available.text == "":
            self.ids.october_available.text = "0"
        if self.ids.november_available.text == "":
            self.ids.november_available.text = "0"
        if self.ids.december_available.text == "":
            self.ids.december_available.text = "0"

    def show(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM income where oid= 1")
        records = c.fetchall()
        for record in records:
            self.ids.inc_1.text = str(record[0])
            self.ids.inc_2.text = str(record[1])
            self.ids.inc_3.text = str(record[2])
            self.ids.inc_4.text = str(record[3])
            self.ids.inc_5.text = str(record[4])
            self.ids.inc_6.text = str(record[5])
            self.ids.inc_7.text = str(record[6])
            self.ids.inc_8.text = str(record[7])
            self.ids.inc_9.text = str(record[8])
            self.ids.inc_10.text = str(record[9])
            self.ids.inc_11.text = str(record[10])
            self.ids.inc_12.text = str(record[11])

        c.execute("SELECT *, oid FROM available where oid= 1")
        records = c.fetchall()
        for record in records:
            self.ids.avail_1.text = str(record[0])
            self.ids.avail_2.text = str(record[1])
            self.ids.avail_3.text = str(record[2])
            self.ids.avail_4.text = str(record[3])
            self.ids.avail_5.text = str(record[4])
            self.ids.avail_6.text = str(record[5])
            self.ids.avail_7.text = str(record[6])
            self.ids.avail_8.text = str(record[7])
            self.ids.avail_9.text = str(record[8])
            self.ids.avail_10.text = str(record[9])
            self.ids.avail_11.text = str(record[10])
            self.ids.avail_12.text = str(record[11])
        conn.commit()
        conn.close()

        self.rule()
        self.submit_cond()

    def edit(self):
        self.ids.submit_report.disabled = True
        self.ids.save_report.disabled = False

        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("SELECT * FROM income WHERE oid = 1")
        records = c.fetchall()
        for record in records:
            january = str(record[0])
            self.ids.january_income.text = january
            february = str(record[1])
            self.ids.february_income.text = february
            march = str(record[2])
            self.ids.march_income.text = march
            april = str(record[3])
            self.ids.april_income.text = april
            may = str(record[4])
            self.ids.may_income.text = may
            june = str(record[5])
            self.ids.june_income.text = june
            july = str(record[6])
            self.ids.july_income.text = july
            august = str(record[7])
            self.ids.august_income.text = august
            september = str(record[8])
            self.ids.september_income.text = september
            october = str(record[9])
            self.ids.october_income.text = october
            november = str(record[10])
            self.ids.november_income.text = november
            december = str(record[11])
            self.ids.december_income.text = december

        c.execute("SELECT * FROM available WHERE oid = 1")
        records2 = c.fetchall()
        for record2 in records2:
            january = str(record2[0])
            self.ids.january_available.text = january
            february = str(record2[1])
            self.ids.february_available.text = february
            march = str(record2[2])
            self.ids.march_available.text = march
            april = str(record2[3])
            self.ids.april_available.text = april
            may = str(record2[4])
            self.ids.may_available.text = may
            june = str(record2[5])
            self.ids.june_available.text = june
            july = str(record2[6])
            self.ids.july_available.text = july
            august = str(record2[7])
            self.ids.august_available.text = august
            september = str(record2[8])
            self.ids.september_available.text = september
            october = str(record2[9])
            self.ids.october_available.text = october
            november = str(record2[10])
            self.ids.november_available.text = november
            december = str(record2[11])
            self.ids.december_available.text = december
        conn.commit()
        conn.close()

    def save(self):
        self.empty_fields_cond()
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("""UPDATE income SET
                                    january = :january,
                                    february = :february,
                                    march = :march,
                                    april = :april,
                                    may = :may,
                                    june = :june,
                                    july = :july,
                                    august = :august,
                                    september = :september,
                                    october = :october,
                                    november = :november,
                                    december = :december

                                    WHERE oid = 1""", {
                   'january': self.ids.january_income.text,
                   'february': self.ids.february_income.text,
                   'march': self.ids.march_income.text,
                   'april': self.ids.april_income.text,
                   'may': self.ids.may_income.text,
                   'june': self.ids.june_income.text,
                   'july': self.ids.july_income.text,
                   'august': self.ids.august_income.text,
                   'september': self.ids.september_income.text,
                   'october': self.ids.october_income.text,
                   'november': self.ids.november_income.text,
                   'december': self.ids.december_income.text})

        c.execute("""UPDATE available SET
                                                january = :january,
                                                february = :february,
                                                march = :march,
                                                april = :april,
                                                may = :may,
                                                june = :june,
                                                july = :july,
                                                august = :august,
                                                september = :september,
                                                october = :october,
                                                november = :november,
                                                december = :december

                                                WHERE oid = 1""", {
            'january': self.ids.january_available.text,
            'february': self.ids.february_available.text,
            'march': self.ids.march_available.text,
            'april': self.ids.april_available.text,
            'may': self.ids.may_available.text,
            'june': self.ids.june_available.text,
            'july': self.ids.july_available.text,
            'august': self.ids.august_available.text,
            'september': self.ids.september_available.text,
            'october': self.ids.october_available.text,
            'november': self.ids.november_available.text,
            'december': self.ids.december_available.text})
        conn.commit()
        conn.close()

        self.clear()
        self.show()
        self.rule()
        self.submit_cond()

        screens[2].export_data()
        screens[2].calculate_left()
        screens[2].calculate_others()

    def delete(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("DELETE FROM income")
        c.execute("DELETE FROM available")
        conn.commit()
        conn.close()

        self.ids.inc_1.text = "0"
        self.ids.inc_2.text = "0"
        self.ids.inc_3.text = "0"
        self.ids.inc_4.text = "0"
        self.ids.inc_5.text = "0"
        self.ids.inc_6.text = "0"
        self.ids.inc_7.text = "0"
        self.ids.inc_8.text = "0"
        self.ids.inc_9.text = "0"
        self.ids.inc_10.text = "0"
        self.ids.inc_11.text = "0"
        self.ids.inc_12.text = "0"

        self.clear()
        self.rule()
        self.submit_cond()

        self.ids.rep_ch_del_1.active = False
        self.ids.rep_ch_del_2.active = False
        self.ids.rep_ch_del_3.active = False

    def delete_cond_rep(self):
        if not self.ids.rep_ch_del_1.active or not self.ids.rep_ch_del_2.active or not self.ids.rep_ch_del_3.active:
            self.ids.delete_report.disabled = True
        else:
            self.ids.delete_report.disabled = False

    def clear(self):
        self.ids.january_income.text = ''
        self.ids.february_income.text = ''
        self.ids.march_income.text = ''
        self.ids.april_income.text = ''
        self.ids.may_income.text = ''
        self.ids.june_income.text = ''
        self.ids.july_income.text = ''
        self.ids.august_income.text = ''
        self.ids.september_income.text = ''
        self.ids.october_income.text = ''
        self.ids.november_income.text = ''
        self.ids.december_income.text = ''

        self.ids.january_available.text = ''
        self.ids.february_available.text = ''
        self.ids.march_available.text = ''
        self.ids.april_available.text = ''
        self.ids.may_available.text = ''
        self.ids.june_available.text = ''
        self.ids.july_available.text = ''
        self.ids.august_available.text = ''
        self.ids.september_available.text = ''
        self.ids.october_available.text = ''
        self.ids.november_available.text = ''
        self.ids.december_available.text = ''

        self.ids.save_report.disabled = True

    def back(self):
        self.clear()
        self.ids.submit_report.disabled = False

    def rule(self):
        if self.ids.inc_1.text == "0" or self.ids.inc_1.text == "":
            self.ids.inc_1.text = "0"
            self.ids.bill_1.text = "0"
            self.ids.after_1.text = "0"
            self.ids.avail_1.text = "0"
            self.ids.oth_1.text = "0"

        if self.ids.inc_2.text == "0" or self.ids.inc_2.text == "":
            self.ids.inc_2.text = "0"
            self.ids.bill_2.text = "0"
            self.ids.after_2.text = "0"
            self.ids.avail_2.text = "0"
            self.ids.oth_2.text = "0"

        if self.ids.inc_3.text == "0" or self.ids.inc_3.text == "":
            self.ids.inc_3.text = "0"
            self.ids.bill_3.text = "0"
            self.ids.after_3.text = "0"
            self.ids.avail_3.text = "0"
            self.ids.oth_3.text = "0"

        if self.ids.inc_4.text == "0" or self.ids.inc_4.text == "":
            self.ids.inc_4.text = "0"
            self.ids.bill_4.text = "0"
            self.ids.after_4.text = "0"
            self.ids.avail_4.text = "0"
            self.ids.oth_4.text = "0"

        if self.ids.inc_5.text == "0" or self.ids.inc_5.text == "":
            self.ids.inc_5.text = "0"
            self.ids.bill_5.text = "0"
            self.ids.after_5.text = "0"
            self.ids.avail_5.text = "0"
            self.ids.oth_5.text = "0"

        if self.ids.inc_6.text == "0" or self.ids.inc_6.text == "":
            self.ids.inc_6.text = "0"
            self.ids.bill_6.text = "0"
            self.ids.after_6.text = "0"
            self.ids.avail_6.text = "0"
            self.ids.oth_6.text = "0"

        if self.ids.inc_7.text == "0" or self.ids.inc_7.text == "":
            self.ids.inc_7.text = "0"
            self.ids.bill_7.text = "0"
            self.ids.after_7.text = "0"
            self.ids.avail_7.text = "0"
            self.ids.oth_7.text = "0"

        if self.ids.inc_8.text == "0" or self.ids.inc_8.text == "":
            self.ids.inc_8.text = "0"
            self.ids.bill_8.text = "0"
            self.ids.after_8.text = "0"
            self.ids.avail_8.text = "0"
            self.ids.oth_8.text = "0"

        if self.ids.inc_9.text == "0" or self.ids.inc_9.text == "":
            self.ids.inc_9.text = "0"
            self.ids.bill_9.text = "0"
            self.ids.after_9.text = "0"
            self.ids.avail_9.text = "0"
            self.ids.oth_9.text = "0"

        if self.ids.inc_10.text == "0" or self.ids.inc_10.text == "":
            self.ids.inc_10.text = "0"
            self.ids.bill_10.text = "0"
            self.ids.after_10.text = "0"
            self.ids.avail_10.text = "0"
            self.ids.oth_10.text = "0"

        if self.ids.inc_11.text == "0" or self.ids.inc_11.text == "":
            self.ids.inc_11.text = "0"
            self.ids.bill_11.text = "0"
            self.ids.after_11.text = "0"
            self.ids.avail_11.text = "0"
            self.ids.oth_11.text = "0"

        if self.ids.inc_12.text == "0" or self.ids.inc_12.text == "":
            self.ids.inc_12.text = "0"
            self.ids.bill_12.text = "0"
            self.ids.after_12.text = "0"
            self.ids.avail_12.text = "0"
            self.ids.oth_12.text = "0"

    def remove_text_on_click_report(self):
        def january():
            if not self.ids.save_report.disabled:
                if self.ids.january_income.focus:
                    self.ids.january_income.text = ''
                if not self.ids.january_income.focus:
                    if self.ids.january_income.text == '':
                        self.ids.january_income.text = self.ids.inc_1.text

                if self.ids.january_available.focus:
                    self.ids.january_available.text = ''
                if not self.ids.january_available.focus:
                    if self.ids.january_available.text == '':
                        self.ids.january_available.text = self.ids.avail_1.text

        def february():
            if not self.ids.save_report.disabled:
                if self.ids.february_income.focus:
                    self.ids.february_income.text = ''
                if not self.ids.february_income.focus:
                    if self.ids.february_income.text == '':
                        self.ids.february_income.text = self.ids.inc_2.text

                if self.ids.february_available.focus:
                    self.ids.february_available.text = ''
                if not self.ids.february_available.focus:
                    if self.ids.february_available.text == '':
                        self.ids.february_available.text = self.ids.avail_2.text

        def march():
            if not self.ids.save_report.disabled:
                if self.ids.march_income.focus:
                    self.ids.march_income.text = ''
                if not self.ids.march_income.focus:
                    if self.ids.march_income.text == '':
                        self.ids.march_income.text = self.ids.inc_3.text

                if self.ids.march_available.focus:
                    self.ids.march_available.text = ''
                if not self.ids.march_available.focus:
                    if self.ids.march_available.text == '':
                        self.ids.march_available.text = self.ids.avail_3.text

        def april():
            if not self.ids.save_report.disabled:
                if self.ids.april_income.focus:
                    self.ids.april_income.text = ''
                if not self.ids.april_income.focus:
                    if self.ids.april_income.text == '':
                        self.ids.april_income.text = self.ids.inc_4.text

                if self.ids.april_available.focus:
                    self.ids.april_available.text = ''
                if not self.ids.april_available.focus:
                    if self.ids.april_available.text == '':
                        self.ids.april_available.text = self.ids.avail_4.text

        def may():
            if not self.ids.save_report.disabled:
                if self.ids.may_income.focus:
                    self.ids.may_income.text = ''
                if not self.ids.may_income.focus:
                    if self.ids.may_income.text == '':
                        self.ids.may_income.text = self.ids.inc_5.text

                if self.ids.may_available.focus:
                    self.ids.may_available.text = ''
                if not self.ids.may_available.focus:
                    if self.ids.may_available.text == '':
                        self.ids.may_available.text = self.ids.avail_5.text

        def june():
            if not self.ids.save_report.disabled:
                if self.ids.june_income.focus:
                    self.ids.june_income.text = ''
                if not self.ids.june_income.focus:
                    if self.ids.june_income.text == '':
                        self.ids.june_income.text = self.ids.inc_6.text

                if self.ids.june_available.focus:
                    self.ids.june_available.text = ''
                if not self.ids.june_available.focus:
                    if self.ids.june_available.text == '':
                        self.ids.june_available.text = self.ids.avail_6.text

        def july():
            if not self.ids.save_report.disabled:
                if self.ids.july_income.focus:
                    self.ids.july_income.text = ''
                if not self.ids.july_income.focus:
                    if self.ids.july_income.text == '':
                        self.ids.july_income.text = self.ids.inc_7.text

                if self.ids.july_available.focus:
                    self.ids.july_available.text = ''
                if not self.ids.july_available.focus:
                    if self.ids.july_available.text == '':
                        self.ids.july_available.text = self.ids.avail_7.text

        def august():
            if not self.ids.save_report.disabled:
                if self.ids.august_income.focus:
                    self.ids.august_income.text = ''
                if not self.ids.august_income.focus:
                    if self.ids.august_income.text == '':
                        self.ids.august_income.text = self.ids.inc_8.text

                if self.ids.august_available.focus:
                    self.ids.august_available.text = ''
                if not self.ids.august_available.focus:
                    if self.ids.august_available.text == '':
                        self.ids.august_available.text = self.ids.avail_8.text

        def september():
            if not self.ids.save_report.disabled:
                if self.ids.september_income.focus:
                    self.ids.september_income.text = ''
                if not self.ids.september_income.focus:
                    if self.ids.september_income.text == '':
                        self.ids.september_income.text = self.ids.inc_9.text

                if self.ids.september_available.focus:
                    self.ids.september_available.text = ''
                if not self.ids.september_available.focus:
                    if self.ids.september_available.text == '':
                        self.ids.september_available.text = self.ids.avail_9.text

        def october():
            if not self.ids.save_report.disabled:
                if self.ids.october_income.focus:
                    self.ids.october_income.text = ''
                if not self.ids.october_income.focus:
                    if self.ids.october_income.text == '':
                        self.ids.october_income.text = self.ids.inc_10.text

                if self.ids.october_available.focus:
                    self.ids.october_available.text = ''
                if not self.ids.october_available.focus:
                    if self.ids.october_available.text == '':
                        self.ids.october_available.text = self.ids.avail_10.text

        def november():
            if not self.ids.save_report.disabled:
                if self.ids.november_income.focus:
                    self.ids.november_income.text = ''
                if not self.ids.november_income.focus:
                    if self.ids.november_income.text == '':
                        self.ids.november_income.text = self.ids.inc_11.text

                if self.ids.november_available.focus:
                    self.ids.november_available.text = ''
                if not self.ids.november_available.focus:
                    if self.ids.november_available.text == '':
                        self.ids.november_available.text = self.ids.avail_11.text

        def december():
            if not self.ids.save_report.disabled:
                if self.ids.december_income.focus:
                    self.ids.december_income.text = ''
                if not self.ids.december_income.focus:
                    if self.ids.december_income.text == '':
                        self.ids.december_income.text = self.ids.inc_12.text

                if self.ids.december_available.focus:
                    self.ids.december_available.text = ''
                if not self.ids.december_available.focus:
                    if self.ids.december_available.text == '':
                        self.ids.december_available.text = self.ids.avail_12.text

        january()
        february()
        march()
        april()
        may()
        june()
        july()
        august()
        september()
        october()
        november()
        december()


class Manager(ScreenManager):
    pass


# Configuring the Username Database + the Kivy Design file + the Screen Manager
kv = Builder.load_file("bills.kv")
db = DataBase("test.txt")
sm = Manager()

# Configuring the screens
screens = [Login(name='login'), CreateAccount(name='create'), Main(name='main'), January(name='january'),
           February(name='february'), March(name='march'), April(name='april'), May(name='may'), June(name='june'),
           July(name='july'), August(name='august'), September(name='september'), October(name='october'),
           November(name='november'), December(name='december'), Report(name='report')]

for screen in screens:
    sm.add_widget(screen)


# Returning all in the Main Application
class BudgetManagerApp(App):
    # Creating the Configuration Build
    def build_config(self, config):
        main_config()

    # Creating the Main App build
    def build(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE if not exists january(
                                                        rent text,
                                                        electricity text,
                                                        heat text,
                                                        water text,
                                                        food text,
                                                        building text,
                                                        internet text,
                                                        goofy text,
                                                        cigarettes text,
                                                        credit text,
                                                        additional text) """)
        c.execute("""CREATE TABLE if not exists february(
                                                        rent text,
                                                        electricity text,
                                                        heat text,
                                                        water text,
                                                        food text,
                                                        building text,
                                                        internet text,
                                                        goofy text,
                                                        cigarettes text,
                                                        credit text,
                                                        additional text) """)
        c.execute("""CREATE TABLE if not exists march(
                                                        rent text,
                                                        electricity text,
                                                        heat text,
                                                        water text,
                                                        food text,
                                                        building text,
                                                        internet text,
                                                        goofy text,
                                                        cigarettes text,
                                                        credit text,
                                                        additional text) """)
        c.execute("""CREATE TABLE if not exists april(
                                                        rent text,
                                                        electricity text,
                                                        heat text,
                                                        water text,
                                                        food text,
                                                        building text,
                                                        internet text,
                                                        goofy text,
                                                        cigarettes text,
                                                        credit text,
                                                        additional text) """)
        c.execute("""CREATE TABLE if not exists may(
                                                        rent text,
                                                        electricity text,
                                                        heat text,
                                                        water text,
                                                        food text,
                                                        building text,
                                                        internet text,
                                                        goofy text,
                                                        cigarettes text,
                                                        credit text,
                                                        additional text) """)
        c.execute("""CREATE TABLE if not exists june(
                                                        rent text,
                                                        electricity text,
                                                        heat text,
                                                        water text,
                                                        food text,
                                                        building text,
                                                        internet text,
                                                        goofy text,
                                                        cigarettes text,
                                                        credit text,
                                                        additional text) """)
        c.execute("""CREATE TABLE if not exists july(
                                                        rent text,
                                                        electricity text,
                                                        heat text,
                                                        water text,
                                                        food text,
                                                        building text,
                                                        internet text,
                                                        goofy text,
                                                        cigarettes text,
                                                        credit text,
                                                        additional text) """)
        c.execute("""CREATE TABLE if not exists august(
                                                        rent text,
                                                        electricity text,
                                                        heat text,
                                                        water text,
                                                        food text,
                                                        building text,
                                                        internet text,
                                                        goofy text,
                                                        cigarettes text,
                                                        credit text,
                                                        additional text) """)
        c.execute("""CREATE TABLE if not exists september(
                                                        rent text,
                                                        electricity text,
                                                        heat text,
                                                        water text,
                                                        food text,
                                                        building text,
                                                        internet text,
                                                        goofy text,
                                                        cigarettes text,
                                                        credit text,
                                                        additional text) """)
        c.execute("""CREATE TABLE if not exists october(
                                                        rent text,
                                                        electricity text,
                                                        heat text,
                                                        water text,
                                                        food text,
                                                        building text,
                                                        internet text,
                                                        goofy text,
                                                        cigarettes text,
                                                        credit text,
                                                        additional text) """)
        c.execute("""CREATE TABLE if not exists november(
                                                        rent text,
                                                        electricity text,
                                                        heat text,
                                                        water text,
                                                        food text,
                                                        building text,
                                                        internet text,
                                                        goofy text,
                                                        cigarettes text,
                                                        credit text,
                                                        additional text) """)
        c.execute("""CREATE TABLE if not exists december(
                                                        rent text,
                                                        electricity text,
                                                        heat text,
                                                        water text,
                                                        food text,
                                                        building text,
                                                        internet text,
                                                        goofy text,
                                                        cigarettes text,
                                                        credit text,
                                                        additional text) """)
        c.execute("""CREATE TABLE if not exists income(
                                                        january text,
                                                        february text,
                                                        march text,
                                                        april text,
                                                        may text,
                                                        june text,
                                                        july text,
                                                        august text,
                                                        september text,
                                                        october text,
                                                        november text,
                                                        december text) """)
        c.execute("""CREATE TABLE if not exists available(
                                                        january text,
                                                        february text,
                                                        march text,
                                                        april text,
                                                        may text,
                                                        june text,
                                                        july text,
                                                        august text,
                                                        september text,
                                                        october text,
                                                        november text,
                                                        december text) """)
        conn.commit()
        conn.close()
        return sm


# Running the Application
if __name__ == '__main__':
    BudgetManagerApp().run()
