package Exercicio4;

import org.hibernate.Session;
import org.hibernate.Transaction;

public class MainApp {
    public static void main(String[] args) {
        Session session = HibernateUtil.getSessionFactory().openSession();
        Transaction tx = null;

        try {
            tx = session.beginTransaction();

            Pedido pedido1 = new Pedido("Compra de Natal");
            Pedido pedido2 = new Pedido("Compra Black Friday");

            Item itemA = new Item("Caneta");
            Item itemB = new Item("Caderno");

            pedido1.addItem(itemA);
            pedido1.addItem(itemB);

            pedido2.addItem(itemA);

            session.persist(pedido1);
            session.persist(pedido2);

            tx.commit();
            System.out.println("Pedidos e Itens salvos com sucesso!");
        } catch (Exception e) {
            if (tx != null) tx.rollback();
            e.printStackTrace();
        } finally {
            session.close();
            HibernateUtil.getSessionFactory().close();
        }
    }
}
