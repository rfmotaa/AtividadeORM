package Exercicio3;

import org.hibernate.Session;
import org.hibernate.Transaction;

public class MainApp {
    public static void main(String[] args) {
        Session session = HibernateUtil.getSessionFactory().openSession();
        Transaction tx = null;

        try {
            tx = session.beginTransaction();

            Cliente cliente = new Cliente("Ana Pereira", "ana@example.com");

            Pedido p1 = new Pedido("Celular", 1500.0);
            Pedido p2 = new Pedido("Notebook", 3500.0);

            cliente.addPedido(p1);
            cliente.addPedido(p2);

            session.persist(cliente);

            tx.commit();
            System.out.println("Cliente e Pedidos salvos com sucesso!");
        } catch (Exception e) {
            if (tx != null) tx.rollback();
            e.printStackTrace();
        } finally {
            session.close();
            HibernateUtil.getSessionFactory().close();
        }
    }
}