package br.unip.sicc.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class GerenciadorConexao {

    private static final String URL
            = "jdbc:derby://192.168.0.97/testdb";
            //= "jdbc:oracle:thin:@db20220718183412_high?TNS_ADMIN=Z:/ALPOO/AULA4/JDBC/Wallet_DB20220718183412";
            //= "jdbc:mysql://127.0.0.1:3306/sakila?zeroDateTimeBehavior=convertToNull&useTimezone=true&serverTimezone=UTC";
    private static final String USUARIO = "app";
            //= "JAVAUSER";
            //= "aluno";
    private static final String SENHA = "app";
            //= "XJPt5Jij5iinCmA";
            //= "unip";

    public static Connection getConnection() 
                            throws DadosException {
        Connection connection = null;
        try {
            connection = 
            DriverManager.getConnection(URL, USUARIO, SENHA);
        } catch (SQLException ex) {
            throw 
            new 
        DadosException("Não foi possível conectar", ex);
        }
        return connection;
    }

    public static void fechar(Connection connection) throws DadosException {
        try {
            connection.close();
        } catch (SQLException ex) {
            throw new DadosException(
                    "Não foi possivel desconectar ao banco de dados",
                    ex);
        }
    }

    public static void fechar(Connection connection,
            Statement statement) throws DadosException {
        try {
            statement.close();
        } catch (SQLException ex) {
            throw new DadosException(
                    "Não foi possivel desconectar ao banco de dados",
                    ex);
        } finally {
            GerenciadorConexao.fechar(connection);
        }
    }

    public static void fechar(Connection connection,
            Statement statement,
            ResultSet resultSet) throws DadosException {
        try {
            resultSet.close();
        } catch (SQLException ex) {
            throw new DadosException(
                    "Não foi possivel desconectar ao banco de dados",
                    ex);
        } finally {
            GerenciadorConexao.fechar(connection, statement);
        }
    }

}
