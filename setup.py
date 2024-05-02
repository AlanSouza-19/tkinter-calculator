from cx_Freeze import setup, Executable


def main():
    setup(
        name='Calculadora',
        version='0.1.1',
        authors=["AlanSouza-19 <souzaalanc75@gmail.com>"],
        description='Calculadora feita em python com a lib TKinter',
        options={
            'build_exe': {
                'includes': ['tkinter', 'math', 're', 'typing'],
            }
        },
        executables=[
            Executable(
                script='./calculadora/main.py',
                base='Win32Gui',
                icon='./icons/calculator-icon',
                target_name='Calculadora'    
            )
        ]
    )

if __name__ == '__main__':
    main()
