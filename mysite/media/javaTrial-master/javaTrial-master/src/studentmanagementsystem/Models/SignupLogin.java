/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package studentmanagementsystem.Models;

import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.ResultSet;
import javax.swing.JOptionPane;

/**
 *
 * @author User
 */
public class SignupLogin  extends Connection{
    
    public String name, pass, pass2;
    
    public SignupLogin(){}
//    
    
    public ResultSet login(){
        
        try{
            PreparedStatement stmt = this.conn.prepareStatement("SELECT * FROM admin WHERE name = ? AND password = ?");
            stmt.setString(1, this.name);
            stmt.setString(2, this.pass);
            
            return stmt.executeQuery();
        }catch(SQLException e){
            
            JOptionPane.showMessageDialog(null, e.getMessage());
            
            return null;
        }
    }
    //registration of the admin
    public int signup(){
        int ret = 0;
        try{
            PreparedStatement stmt = this.conn.prepareStatement("INSERT INTO admin (name, password) VALUES (?, ?)");
            stmt.setString(1, this.name);
            stmt.setString(2, this.pass);
            
            ret = stmt.executeUpdate();
            
        }catch(Exception e){
            
            JOptionPane.showMessageDialog(null, e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
            
        }
        return ret;
    }
    
    //check if the username already exist in the database
    public ResultSet nameChecker(){
        
        try{
            PreparedStatement stmt = this.conn.prepareStatement("SELECT * FROM admin WHERE name = ?");
            stmt.setString(1, this.name);
            return stmt.executeQuery();
            
        }catch(Exception e){
            
            JOptionPane.showMessageDialog(null, e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
            
            return null;
        }
    }
    
}
