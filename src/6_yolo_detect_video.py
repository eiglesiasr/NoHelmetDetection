import cv2
import argparse
from ultralytics import YOLO

def main(video_path, model_path, conf_threshold):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"❌ Error: no se pudo abrir el video '{video_path}'")
        return

    model = YOLO(model_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model.predict(source=frame, conf=conf_threshold, stream=True)

        for r in results:
            annotated_frame = r.plot()

        cv2.imshow("YOLOv8 Predictions", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run YOLOv8 inference on a video file.")
    parser.add_argument("--video", required=True, help="Path to input video file")
    parser.add_argument("--model", required=True, help="Path to YOLO model (.pt)")
    parser.add_argument("--conf", type=float, default=0.3, help="Confidence threshold")

    args = parser.parse_args()
    main(args.video, args.model, args.conf)
# Usage: python src/6_yolo_detect_video.py --video path/to/video.mp4 --model path/to/yolo_model.pt --conf 0.3