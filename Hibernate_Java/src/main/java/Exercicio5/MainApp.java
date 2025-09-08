package Exercicio5;

import org.hibernate.Session;
import org.hibernate.Transaction;

public class MainApp {
    public static void main(String[] args) {
        Session session = HibernateUtil.getSessionFactory().openSession();
        Transaction tx = null;

        try {
            tx = session.beginTransaction();

            ClienteFisico cf = new ClienteFisico("Maria Fisica", "maria@ex.com", "123.456.789-00");
            ClienteJuridico cj = new ClienteJuridico("Empresa X", "contato@empresa.com", "12.345.678/0001-99");

            session.persist(cf);
            session.persist(cj);

            tx.commit();
            System.out.println("Clientes salvos com herança com sucesso!");
        } catch (Exception e) {
            if (tx != null) tx.rollback();
            e.printStackTrace();
        } finally {
            session.close();
            HibernateUtil.getSessionFactory().close();
        }
    }
}
