


class Node:
    def __init__ (
            self, 
            left=None, 
            right=None, 
            val=0
            ) -> None:
        self.left=left
        self.right=right
        self.val=val


def valid_btree ( root: Node ) -> bool:
    
    if root is None:
        return False

    if root.left is None and \
        root.right is None:
        return True

    if root.left is None or \
        root.right is None:
        return False

    if root.left.val > root.val or \
        root.right < root.val:
        return False
    
    return valid_btree( root.left ) and \
        valid_btree( root.right )


