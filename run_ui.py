import streamlit as st
from streamlit_env_check import check_env
from tabs import tab_tiles

def run():
    st.set_page_config(page_title="ThreadParser", layout="wide")
    st.sidebar.title("⚙️ Settings")
    if st.sidebar.button("🧪 Run Diagnostic Test"):
        from validators.test_threadparser_dashboard import check_files, test_csv_parsing, check_import, suggest_fixes
        check_files()
        test_csv_parsing()
        check_import("tabs/tab_tiles.py", "tab_tiles")
        check_import("sync/applet_matrix_loader.py", "applet_matrix_loader")
        check_import("validators/tile_status_engine.py", "tile_status_engine")
        suggest_fixes()
        st.stop()

    check_env()
    tab_tiles

if __name__ == '__main__':
    run()