package Exercicio2;

import org.hibernate.Session;
import org.hibernate.Transaction;

public class MainApp {
    public static void main(String[] args) {
        Session session = HibernateUtil.getSessionFactory().openSession();
        Transaction tx = null;

        try {
            tx = session.beginTransaction();

            Endereco endereco = new Endereco("Rua das Flores", "São Paulo", "SP");
            Cliente cliente = new Cliente("João da Silva", "joao@example.com", endereco);

            session.persist(cliente);

            tx.commit();
            System.out.println("Cliente e Endereco salvos com sucesso!");
        } catch (Exception e) {
            if (tx != null) tx.rollback();
            e.printStackTrace();
        } finally {
            session.close();
            HibernateUtil.getSessionFactory().close();
        }
    }
}
