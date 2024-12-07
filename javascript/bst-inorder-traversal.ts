class TreeNode {
   val: number
   left: TreeNode | null
   right: TreeNode | null
   constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
      this.val = (val === undefined ? 0 : val)
      this.left = (left === undefined ? null : left)
      this.right = (right === undefined ? null : right)
   }
}



function inorderTraversal(root: TreeNode | null): number[] {

   function inorder(root?: TreeNode | null): number[] {
      if (!root) {
         return []
      }

      const res: any[] = []
      const stack: Array<TreeNode | null> = []

      while (root || stack.length > 0) {
         while (root) {
            stack.push(root)
            root = root.left
         }

         root = stack.pop() as TreeNode
         res.push(root.val)
         root = root.right

      }

      return res
   }

   const res = inorder(root)
   return res
};
