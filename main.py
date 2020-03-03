import scraping
import gui

def main():

    #入力ウインドウを生成する
    input_gui = gui.Scraping_GUI()
    input_gui.generate_window()
    keyword, areaword = input_gui.event_loop()

    #入力結果をもとにpandas dataframeを生成する
    scr = scraping.Scraping(keyword, areaword)
    scr.open_browser()
    scr.show_more_btn_click()
    store_is_none = scr.get_store_list()

    if store_is_none == -1:
        scr.close()
        input_gui.store_is_none()
        return -1
    
    #file_name =scr.output_CSV()
    df = scr.output_dataframe()
    scr.close()

    #出力ウインドウを生成する
    output_gui = gui.Output_GUI(df)
    output_gui.output()

if __name__ == '__main__':
    main()
