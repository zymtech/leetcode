package binaryTree;



/**
 * Created by Administrator on 10/5/2016.
 */
public class lowestCommonAncestorOfaBinaryTree {
    TreeNode lca;
    TreeNode other;
    boolean containOther(TreeNode root){
        if (root == null) return false;
        if (root == other) return true;
        return containOther(root.left) || containOther(root.right);
    }
    void inorder(TreeNode root, TreeNode p, TreeNode q){
        if (lca != null) return;
        if (root == null) return ;
        if (other == null) inorder(root.left, p, q);
        if (other == null){
            if (root == p){
                other = q;
            }else if (root == q){
                other = p;
            }
        }
        if (other != null) {
            if (root == other || containOther(root.right)){
                lca = root;
            }
        }
        if (other == null){
            inorder(root.right, p, q);
        }
    }
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q){
        inorder(root, p, q);
        return lca;
    }

    public static void main(String[] args){
        TreeNode root = new TreeNode(3);
        TreeNode p = new TreeNode(1);
        TreeNode q = new TreeNode(2);
        lowestCommonAncestorOfaBinaryTree test = new lowestCommonAncestorOfaBinaryTree();
        test.lowestCommonAncestor(root,p,q);

    }
}


