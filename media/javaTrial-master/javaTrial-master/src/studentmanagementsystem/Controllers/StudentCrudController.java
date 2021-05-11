/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package studentmanagementsystem.Controllers;

import studentmanagementsystem.Models.Student;
import java.net.URL;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ResourceBundle;
import javafx.fxml.Initializable;
import javafx.scene.control.ComboBox;
import javafx.fxml.FXML;
import javafx.scene.control.DatePicker;
import javafx.scene.control.TextField;
import javafx.scene.control.Button;
import javafx.stage.Stage;
import javax.swing.JOptionPane;
import studentmanagementsystem.Models.GradeSection;

/**
 * FXML Controller class
 *
 * @author User
 */
public class StudentCrudController implements Initializable {

    /**
     * Initializes the controller class.
     */
    
    @FXML
    public TextField uname, address;
    @FXML
    public ComboBox gradeSec, religion, gender;
    @FXML
    public DatePicker bdate;
    @FXML
    public Button add, edit;
    @FXML
    public int id;
    
   
    @FXML
    public void studentRegistration(){
      
        Student student = new Student();
        student.name = uname.getText();
        student.address = address.getText();
        student.gradesec = gradeSec.getValue().toString();
        student.religion = religion.getValue().toString();
        student.bdate = bdate.getValue().toString();
        student.gender = gender.getValue().toString();
   
             //get the current window
            Stage stage = (Stage) add.getScene().getWindow();
            // do what you have to do
          
            stage.close();
            // do what you have to do
              int ret = student.addStudent();
       
        if(ret > 0){
            
              JOptionPane.showMessageDialog(null, "Student added successfully", "Success", JOptionPane.INFORMATION_MESSAGE);

        }else{
            
              JOptionPane.showMessageDialog(null,"Error in adding student", "Error", JOptionPane.ERROR_MESSAGE);
              
        }
  
           
    }
    @FXML
    public void editStudent(){
        Student student = new Student();
        student.name = uname.getText();
        student.address = address.getText();
        student.gradesec = gradeSec.getValue().toString();
        student.religion = religion.getValue().toString();
        student.bdate = bdate.getValue().toString();
        student.gender = gender.getValue().toString();
        student.id = this.id;
         //get the current window
            Stage stage = (Stage) add.getScene().getWindow();
            // do what you have to do
          
            stage.close();
        // do what you have to do
        int ret = student.studentEdit();
       
        if(ret > 0){
            
              JOptionPane.showMessageDialog(null, "Edited successfully", "Success", JOptionPane.INFORMATION_MESSAGE);

        }else{
            
              JOptionPane.showMessageDialog(null,"Error in editing student", "Error", JOptionPane.ERROR_MESSAGE);
              
        }
    }
   
   @FXML
     public void setGradeSection(){
         GradeSection gradesec = new GradeSection();
         try{
              ResultSet res = gradesec.getGradeandSection();
                while(res.next()){
                    gradeSec.getItems().addAll(new GradeSection(res.getString("gradesec")).getGradesec());
                }
         }catch(SQLException e){
             
             JOptionPane.showMessageDialog(null,e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
         }
       
        
     }
    
    @Override
    public void initialize(URL url, ResourceBundle rb) {
      

         setGradeSection();
          gender.getItems().addAll("Male", "Female");
          religion.getItems().addAll("Roman Catholic", "Muslim" , "Born Again");
      
     }
     
            
    }    
   

