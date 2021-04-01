/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package studentmanagementsystem.Models;

import java.sql.DriverManager;
import java.sql.SQLException;
import javax.swing.JOptionPane;

/**
 *
 * @author User
 */
public class Connection {
      protected java.sql.Connection conn = null;
    
   public Connection(){
       
       try{
         
           Class.forName("com.mysql.cj.jdbc.Driver");
           // this.con = DriverManager.getConnection("jdbc:mysql://localhost:3306/rtmv?serverTimezone=UTC", "root", "");
           this.conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/java?useSSL=false&serverTimezone=Asia/Manila", "root", "");
           //JOptionPane.showMessageDialog(null, "Connected successfully", "Connected", JOptionPane.INFORMATION_MESSAGE);
           
                                
        }catch(SQLException | ClassNotFoundException e){
            
             JOptionPane.showMessageDialog(null, e.getMessage(), "Error occurred", JOptionPane.ERROR_MESSAGE);
           
        }
       
   }
}
