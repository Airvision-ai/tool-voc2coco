

import argparse
from pathlib import Path

from voc2coco import convert_xmls_to_cocojson, get_label2id


def main():
    parser = argparse.ArgumentParser(
        description="This script processes a single directory with VOC format XML files and converts them to COCO format JSON."
    )
    parser.add_argument("--dir", type=str)
    parser.add_argument('--labels', type=str, help='path to label list.')
    
    args = parser.parse_args()

    label2id = get_label2id(labels_path=args.labels)
    dir = Path(args.dir)
    
    # Generate a list of all XML files in the directory
    xml_files = list(dir.glob("*.xml"))
    convert_xmls_to_cocojson(
        annotation_paths=xml_files,
        label2id=label2id,
        output_jsonpath=dir.parent / f"annotations.coco.json",
    )
    
    
if __name__ == '__main__':
    main()
