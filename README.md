<!-- open a terminal (ctrl+`) and run the below commands to setup your local environment
 
cd to the CHatbot project directory ( for Ex: d:/Project/Chatbot II/Chatbot/ )

run this below line for installing virtual env -->

python -m venv venv

<!-- then activate the venv.

After that run, -->

uvicorn main:app --reload

<!-- your terminal might look similar to below -->

=============================================================================================

D:\Project\Chatbot II\Chatbot>"d:/Project/Chatbot II/Chatbot/.venv/Scripts/activate.bat"

(.venv) D:\Project\Chatbot II\Chatbot>uvicorn main:app --reload
INFO:     Will watch for changes in these directories: ['D:\\Project\\Chatbot II\\Chatbot']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12280] using statreload
INFO:     Started server process [14992]
INFO:     Waiting for application startup.
INFO:     Application startup complete.

=============================================================================================