const CLE = "france.pmtiles";

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (request.method === "POST" && url.pathname === "/create") {
      const mpu = await env.BUCKET.createMultipartUpload(CLE, {
        httpMetadata: { contentType: "application/octet-stream" },
      });
      return Response.json({ uploadId: mpu.uploadId });
    }

    if (request.method === "PUT" && url.pathname === "/part") {
      const uploadId = url.searchParams.get("uploadId");
      const n = Number(url.searchParams.get("n"));
      const mpu = env.BUCKET.resumeMultipartUpload(CLE, uploadId);
      const part = await mpu.uploadPart(n, request.body);
      return Response.json({ partNumber: part.partNumber, etag: part.etag });
    }

    if (request.method === "POST" && url.pathname === "/complete") {
      const { uploadId, parts } = await request.json();
      const mpu = env.BUCKET.resumeMultipartUpload(CLE, uploadId);
      const obj = await mpu.complete(parts);
      return Response.json({ key: obj.key, size: obj.size, etag: obj.etag });
    }

    return new Response("routes: POST /create, PUT /part?uploadId&n, POST /complete", { status: 404 });
  },
};
