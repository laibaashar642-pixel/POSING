
import argparse
from posingargparse  import run_pose
def main():

    parser = argparse.ArgumentParser(description="CV Pipeline")

    parser.add_argument(
        "--task",
        type=str,
        required=True,
        choices=["pose"],
    )

    parser.add_argument("--model", required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--project", required=True)
    parser.add_argument("--conf", type=float, default=0.5)

    args = parser.parse_args()

    if args.task == "pose":

      print("Source from argparse:", args.source)
   
    run_pose(
            model_path=args.model,
            source=args.source,
            conf=args.conf,
            save_dir=args.project
        )
     
if __name__ == "__main__":
    main()