import shutil
import auto_configs as conf


def copy_result():
    shutil.copy(conf.TEMP_DIR + '/segoeui.ttf', conf.RESULT_DIR)
    shutil.copy(conf.TEMP_DIR + '/segoeuib.ttf', conf.RESULT_DIR)
    shutil.copy(conf.TEMP_DIR + '/segoeuil.ttf', conf.RESULT_DIR)
