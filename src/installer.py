from downloader import download
from utils import string_utils
from utils import file_explorer


def install():
    """
    First procedure: ask the user the location of the file(s)
    """
    temp_files = []
    src_file_location = string_utils.non_null_input("Enter the location of the" +
                                                     " file (http/https for url): ")
    
    if string_utils.starts_with_any_value_in(src_file_location, ['http://', 'https://']):
        downloaded_file_path = download(src_file_location)
        if downloaded_file_path != None:
            temp_files.append(downloaded_file_path)
            app_name = string_utils.non_null_input("Enter the app name: ")
            app_version = string_utils.non_null_input("Enter it's version: ")
            app_form = string_utils.either(message="Is the app gui or cli ?: ", first_string="gui", second_string="cli", low=True)
            app_file_form = string_utils.any_of(message="What kind of application file this is (executable: exe, script: s, zip file: z): ",
                                                 values={'exe', 's', 'z'}, low=True)
            
            match app_file_form:
                case 'z':
                    extracted_folder_name = f'{app_name}_temp.extracted'
                    temp_app_folder = file_explorer.extract_zip(downloaded_file_path, extracted_folder_name, error_message_prefix=f'Unable to extract downloaded file: {downloaded_file_path} ')
                    if temp_app_folder != None:
                        temp_files.append(temp_app_folder)
                        file_explorer.show_directory_structure(temp_app_folder)
                        main_exec_path = string_utils.input_starts_with("Enter the path of the main executable. It should start with a slash (/): ", '/')
                        

install()