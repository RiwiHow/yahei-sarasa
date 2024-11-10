import auto_configs as conf
import fetch_original as fetch
import generate_fonts as gen
import copy_result as copy


if __name__ == '__main__':
    fetch.clear_dir(conf.TEMP_DIR)
    fetch.clear_dir(conf.RESULT_DIR)

    url = fetch.get_latest()
    print('========> Latest url: ' + url)
    path = fetch.download(url)
    print('\n========> Download finished')
    fetch.unzip(path)
    print('========> Unzip finished')
    gen.gen_regular()
    print('========> Regular generated')
    gen.gen_bold()
    print('========> Bold generated')
    gen.gen_light()
    print('========> Light generated')
    copy.copy_result()
    print('========> Copy Finished')
