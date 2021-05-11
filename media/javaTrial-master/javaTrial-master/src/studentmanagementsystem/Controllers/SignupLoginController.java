/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package studentmanagementsystem.Controllers;

import java.net.URL;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ResourceBundle;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.control.PasswordField;
import javafx.stage.Stage;
import javax.swing.JOptionPane;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import studentmanagementsystem.Models.*;

/**
 *
 * @author User
 */
public class SignupLoginController implements Initializable {
    @FXML
    private Button openSignupBtn, signup;
    
    @FXML
    private TextField uname;
    
    @FXML
    private PasswordField pass, pass2;
    
    @FXML
    public void login() throws SQLException{
        SignupLogin login = new SignupLogin();
        login.name = uname.getText();
        login.pass = pass.getText();
        
        ResultSet ret = login.login();
        
        if(ret.next()){
            try{
                FXMLLoader fxml = new FXMLLoader(getClass().getResource("FXMLS/ManageStudent.fxml"));
                Parent managestudent = (Parent) fxml.load();
                  Stage student = new Stage();
                student.setTitle("Admin Panel");
                student.setResizable(false);
                student.setScene(new Scene(managestudent));

                student.show();
                Stage stage = (Stage) openSignupBtn.getScene().getWindow();
                stage.close();
            }catch(Exception e){
                
                
            }
            

            
        }else{
            
            JOptionPane.showMessageDialog(null, "Incorrect username or password!", "Error", JOptionPane.ERROR_MESSAGE);        }

    }
    
    @FXML
    public void register(){
        
        SignupLogin register = new SignupLogin();
        register.name = uname.getText();
        register.pass = pass.getText();
        //set the matcher for the name to check if its only contain letter
        Pattern letters = Pattern.compile("^[ A-Za-z]+$");
        Matcher matcher = letters.matcher(uname.getText());
     
        int ret;
        if(uname.getText().equals("")){
            
            JOptionPane.showMessageDialog(null,"Username must not be empty!", "Error", JOptionPane.INFORMATION_MESSAGE);
            
        }else{
            //check if name match with the above variable letters
            if(matcher.matches()){
                  if(!pass.getText().equals("")){
                
                        if(pass.getText().equals(pass2.getText())){

                            //call the function that chek if the name inputted is alredy exist
                            ResultSet res = register.nameChecker();

                            try{

                                //check if the return data has an  valeu
                                if(res.next()){

                                     JOptionPane.showMessageDialog(null,"The name " +uname.getText()+" already exist!", "Error", JOptionPane.ERROR_MESSAGE);

                                }else{

                                    //call the function for the signup if the name is not exist in the database
                                     ret = register.signup();

                                     //check if the return value is greater than 0 if true data is inserted to database
                                    if(ret > 0){

                                         JOptionPane.showMessageDialog(null,"Registered successfully you can now login", "Error", JOptionPane.INFORMATION_MESSAGE);
                                         openLoginForm();
                                    }else{

                                         JOptionPane.showMessageDialog(null,"An error has occurred!", "Error", JOptionPane.ERROR_MESSAGE);
                                    }

                                }                     
                            }catch(Exception e){

                                JOptionPane.showMessageDialog(null,"An error has occurred!", "Error", JOptionPane.ERROR_MESSAGE);
                            }




                        }else{

                             JOptionPane.showMessageDialog(null,"Password didn't matched!", "Error", JOptionPane.ERROR_MESSAGE);
                        }


                    }else{

                        JOptionPane.showMessageDialog(null,"Password must not be empty!", "Error", JOptionPane.ERROR_MESSAGE);

                    }
                          
            }else{
                
                 JOptionPane.showMessageDialog(null,"Name must contain letters only!", "Error", JOptionPane.ERROR_MESSAGE);
                
            }//end for checking if name contain only letters
          
        }//end for the checking if name is empty
        
    }//function register end
    @FXML
    public void openLoginForm(){
         try{
           
            FXMLLoader fxmlloader = new FXMLLoader(getClass().getResource("FXMLS/Login.fxml"));
            Parent root1 = (Parent) fxmlloader.load();
            Stage login = new Stage();
            login.setTitle("Login");
            login.setResizable(false);
            
            login.setScene(new Scene(root1)); 
            closeSignup();
            login.show();
            //closeLogin();
           
        } catch(Exception e) {
            
            e.printStackTrace();
            
        }
    }
    //open the signup form
    @FXML
    public void openSignupForm(){
         try{
           
            FXMLLoader fxmlloader = new FXMLLoader(getClass().getResource("FXMLS/Signup.fxml"));
            Parent root1 = (Parent) fxmlloader.load();
            Stage signup = new Stage();
            signup.setTitle("Signup");
            signup.setResizable(false);
            
            signup.setScene(new Scene(root1)); 
            closeLogin();
            signup.show();
            //closeLogin();
           
        } catch(Exception e) {
            
            e.printStackTrace();
            
        }
        
    }
    @FXML
    public void closeLogin(){
        
        Stage stageLogin = (Stage) openSignupBtn.getScene().getWindow();     
        stageLogin.close();
    }
    
     @FXML
    public void closeSignup(){
        
        Stage stageSignup = (Stage) signup.getScene().getWindow();     
        stageSignup.close();
    }
    
    
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        // TODO
    }    
    
}
