from  nodo import Nodo

def huffman_encode(file_path, tabla_huffman):
    compressed = ""
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f.readlines():
            for char in line:
                codigo = tabla_huffman[char]
                compressed += codigo

    return compressed

def write_to_disk(output_file_path, compressed):
    with open(output_file_path, "ab") as f:
        for i in range(0, len(compressed), 8):
            byte_str = compressed[i:i+8]
            if len(byte_str) < 8:
                byte_str = byte_str.ljust(8, "0")
            new_code = int(byte_str, 2)
            int_bytes = new_code.to_bytes(1, "big")
            f.write(int_bytes)

def load_from_disk(filepath) -> str:
    with open(filepath, 'rb') as f:
        binary_data = f.read()

    binary_string_parts = []
    for byte in binary_data:
        binary_string_parts.append(format(byte, '08b'))

    full_binary_string = "".join(binary_string_parts)

    return full_binary_string

def decode_huffman_string(compressed: str, tree_root: Nodo):
    plain_text = ""
    current_char = ""
    current_node: Nodo = tree_root

    for char in compressed:
        if char == "0":
            if current_node.izquierda is not None:
                current_node = current_node.izquierda
            else:
                plain_text += current_node.char
                current_node = tree_root.izquierda
        else:
            if current_node.derecha is not None:
                current_node = current_node.derecha
            else:
                plain_text += current_node.char
                current_node = tree_root.derecha

    return plain_text