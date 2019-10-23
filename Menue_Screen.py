
WindowManager:
  MainScreen:
  AddScreen:
  AddFood:
  DeleteFood:
  Admin:

<MainScreen>:
  name: "MainScreen_name"

  GridLayout:
    cols:1
    GridLayout:
      cols:2
      Label:
        Button:
          text:"add new food"
          size: 300,200
          pos: 0,200
          on_release:
            app.root.current = "AddFood_name"
      Label:
        Button:
          text: "delete food"
          size: 300,200
          pos: 500,200
          on_release:
            app.root.current = "DeleteFood_name"
        Button:
          text: "log in as admin"
          on_release:
            app.root.current = "Admin_name"
<AddFood>:
  name: "AddFood_name"
  GridLayout:
    cols: 2
    Label:
      Button:

        size: 50,50
        pos: 100,100
      Button:
        text: "Tütten"
        size:50,50
        pos: 50,50
        on_release:
          app.root.current = "MainScreen_name"


<DeleteFood>:
  name: "DeleteFood_name"
  Button:
    text: "go back"
    on_release:
      app.root.current = "MainScreen_name"

<Admin>
  name: "Admin_name"
  cols :2
  StackLayout:
    Button:
      text:"eins"
    Button:
      text: "zwei"


<AddScreen>:
 
  name: "AddScreen_name"
  Button:
    text:"go back"
    on_release:
      app.root.current = "MainScreen_name"
