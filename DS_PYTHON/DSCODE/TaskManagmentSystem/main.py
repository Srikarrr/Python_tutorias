class main:

      def main():
          task_service= task_service()
          user_service= user_service()

          user_service.add_user(123,"srikar","srikar544@gmail.com")

          task_service.create_task(1,"Teach DS Basic","Teach from scratch")
          task_service.create_task(2,"Teach DS Basic","scratch")
          task_service.create_task(3,"Do a project","scratch")
          print(task_service.complete_task())

          history = task_service.get_task_history()
          for i in range(history.is_empty()):
               print(history.pop().title)
        
       