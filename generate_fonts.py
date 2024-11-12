import fontforge as ff
import shutil as fs
import auto_configs as conf


def open_font(path):
    return ff.open(path)


def remove_gasp(font):
    font.gasp = ()


def set_cleartype(font):
    font.head_optimized_for_cleartype = 1


def get_version(font):
    return font.version.split(';')[0]


def set_regular_ui_names(font):
    font.fontname = 'SegoeUI'
    font.familyname = 'Segoe UI'
    font.fullname = 'Segoe UI'
    font.version = get_version(font)
    font.copyright = conf.COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Family', 'Segoe UI'),
        ('English (US)', 'Fullname', 'Segoe UI'),
        ('English (US)', 'UniqueID', 'Segoe UI Regular'),
        ('English (US)', 'SubFamily', 'Regular'),
        ('English (US)', 'Version', get_version(font)),
        ('English (US)', 'Copyright', conf.COPYRIGHT)
    )


def set_bold_ui_names(font):
    font.fontname = 'SegoeUI-Bold'
    font.familyname = 'Segoe UI'
    font.fullname = 'Segoe UI Bold'
    font.version = get_version(font)
    font.copyright = conf.COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Family', 'Segoe UI'),
        ('English (US)', 'Fullname', 'Segoe UI Bold'),
        ('English (US)', 'UniqueID', 'Segoe UI Bold'),
        ('English (US)', 'SubFamily', 'Bold'),
        ('English (US)', 'Version', get_version(font)),
        ('English (US)', 'Copyright', conf.COPYRIGHT)
    )


def set_light_ui_names(font):
    font.fontname = 'SegoeUI-Light'
    font.familyname = 'Segoe UI Light'
    font.fullname = 'Segoe UI Light'
    font.version = get_version(font)
    font.copyright = conf.COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Family', 'Segoe UI Light'),
        ('English (US)', 'Fullname', 'Segoe UI Light'),
        ('English (US)', 'UniqueID', 'Segoe UI Light'),
        ('English (US)', 'SubFamily', 'Regular'),
        ('English (US)', 'Version', get_version(font)),
        ('English (US)', 'Copyright', conf.COPYRIGHT)
    )


def gen_regular():
    font_ui = open_font(conf.TEMP_DIR + '/' + conf.REGULAR_SOURCE + '.ttf')
    remove_gasp(font_ui)
    set_cleartype(font_ui)
    set_regular_ui_names(font_ui)

    font_ui.generate(conf.TEMP_DIR + '/segoeui.ttf')


def gen_bold():
    font_ui = open_font(conf.TEMP_DIR + '/' + conf.BOLD_SOURCE + '.ttf')
    remove_gasp(font_ui)
    set_cleartype(font_ui)
    set_bold_ui_names(font_ui)

    font_ui.generate(conf.TEMP_DIR + '/segoeuib.ttf')


def gen_light():
    font_ui = open_font(conf.TEMP_DIR + '/' + conf.LIGHT_SOURCE + '.ttf')
    remove_gasp(font_ui)
    set_cleartype(font_ui)
    set_light_ui_names(font_ui)

    font_ui.generate(conf.TEMP_DIR + '/segoeuil.ttf')
