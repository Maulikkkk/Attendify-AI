import sys
import types

if 'pkg_resources' not in sys.modules:
    import importlib.metadata
    pkg = types.ModuleType('pkg_resources')
    
    def resource_filename(package_or_requirement, resource_name):
        import importlib.util, os
        spec = importlib.util.find_spec(package_or_requirement)
        return os.path.join(os.path.dirname(spec.origin), resource_name)
    
    def get_distribution(dist):
        class Dist:
            version = importlib.metadata.version(dist)
        return Dist()
    
    pkg.resource_filename = resource_filename
    pkg.get_distribution = get_distribution
    sys.modules['pkg_resources'] = pkg

import streamlit as st
from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen
from src.components.dialog_auto_enroll import auto_enroll_dialog

def main():
    st.set_page_config(
        page_title='Attendify AI - Making Attendance faster with AI',
        page_icon= "https://i.ibb.co/YTYGn5qV/logo.png"
    )
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()

        case 'student':
            student_screen()
        
        case None:
            home_screen()

    join_code = st.query_params.get('join-code')
    if join_code:
        if st.session_state.login_type != 'student':
            st.session_state.login_type = 'student'
            st.rerun()
        if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(join_code)

main()